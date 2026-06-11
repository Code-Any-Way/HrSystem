from io import BytesIO
from django.http import HttpResponse
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

from accounts.models import Role
from accounts.permissions import IsHRManager
from payroll.models import PayrollRun, PayrollDetail, PayrollRunStatus
from payroll.serializers import (
    PayrollRunSerializer, 
    PayrollDetailSerializer, 
    PayrollGenerateSerializer
)
from payroll.services import PayrollService

class PayrollRunViewSet(viewsets.ModelViewSet):
    serializer_class = PayrollRunSerializer
    permission_classes = [IsAuthenticated, IsHRManager]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['month', 'year', 'status']

    def get_queryset(self):
        user = self.request.user
        if user.role == Role.SUPER_ADMIN:
            return PayrollRun.objects.all()
        if user.company:
            return PayrollRun.objects.filter(company=user.company)
        return PayrollRun.objects.none()

    @action(detail=False, methods=['post'], url_path='generate')
    def generate_payroll(self, request):
        serializer = PayrollGenerateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = request.user
        if not user.company:
            return Response(
                {"detail": "Your user account is not associated with any company."},
                status=status.HTTP_400_BAD_REQUEST
            )

        month = serializer.validated_data['month']
        year = serializer.validated_data['year']

        try:
            payroll_run, details = PayrollService.generate_monthly_payroll(
                company=user.company,
                month=month,
                year=year
            )
            return Response(PayrollRunSerializer(payroll_run).data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], url_path='approve')
    def approve_payroll(self, request, pk=None):
        payroll_run = self.get_object()
        if payroll_run.status != PayrollRunStatus.DRAFT:
            return Response(
                {"detail": "Payroll run is not in Draft state."},
                status=status.HTTP_400_BAD_REQUEST
            )
        payroll_run.status = PayrollRunStatus.APPROVED
        payroll_run.save()
        return Response(PayrollRunSerializer(payroll_run).data)

class PayrollDetailViewSet(viewsets.ModelViewSet):
    serializer_class = PayrollDetailSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['payroll_run', 'employee']
    ordering_fields = ['net_salary']

    def get_queryset(self):
        user = self.request.user
        if user.role == Role.SUPER_ADMIN:
            return PayrollDetail.objects.all()
        if user.role in [Role.COMPANY_ADMIN, Role.HR_MANAGER]:
            return PayrollDetail.objects.filter(payroll_run__company=user.company)
        # Employees view their own details
        return PayrollDetail.objects.filter(employee__user=user)

    def get_permissions(self):
        if self.action in ['retrieve', 'list', 'export_pdf']:
            return [IsAuthenticated()]
        return [IsAuthenticated(), IsHRManager()]

    @action(detail=True, methods=['get'], url_path='export-pdf')
    def export_pdf(self, request, pk=None):
        detail = self.get_object()
        
        # Enforce that normal employees can only download their own payslip
        if request.user.role == Role.EMPLOYEE and detail.employee.user != request.user:
            return Response({"detail": "Access denied."}, status=status.HTTP_430_FORBIDDEN if hasattr(status, 'HTTP_430_FORBIDDEN') else 403)

        response = HttpResponse(content_type='application/pdf')
        filename = f"payslip_{detail.employee.employee_code}_{detail.payroll_run.year}_{detail.payroll_run.month}.pdf"
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        buffer = BytesIO()
        doc = SimpleDocTemplate(
            buffer, 
            pagesize=letter, 
            rightMargin=36, 
            leftMargin=36, 
            topMargin=36, 
            bottomMargin=36
        )
        
        story = []
        styles = getSampleStyleSheet()
        
        title_style = ParagraphStyle(
            'PayslipTitle',
            parent=styles['Heading1'],
            fontSize=22,
            spaceAfter=15,
            textColor=colors.HexColor("#1e3a8a") # Sleek deep blue
        )
        
        body_style = ParagraphStyle(
            'PayslipBody',
            parent=styles['Normal'],
            fontSize=10,
            spaceAfter=8
        )
        
        header_style = ParagraphStyle(
            'PayslipHeader',
            parent=styles['Heading3'],
            fontSize=12,
            spaceAfter=10,
            textColor=colors.HexColor("#0f172a")
        )

        story.append(Paragraph("HRMS MONTHLY PAYSLIP", title_style))
        story.append(Paragraph(f"<b>Company:</b> {detail.payroll_run.company.name}", body_style))
        story.append(Paragraph(f"<b>Pay Period:</b> {detail.payroll_run.year} - Month {detail.payroll_run.month:02d}", body_style))
        story.append(Spacer(1, 15))

        story.append(Paragraph("Employee Details", header_style))
        emp_data = [
            [Paragraph("<b>Employee Code</b>", body_style), Paragraph(detail.employee.employee_code, body_style)],
            [Paragraph("<b>Employee Name</b>", body_style), Paragraph(f"{detail.employee.first_name} {detail.employee.last_name}", body_style)],
            [Paragraph("<b>Job Title</b>", body_style), Paragraph(detail.employee.job_title, body_style)],
            [Paragraph("<b>Department</b>", body_style), Paragraph(detail.employee.department.name, body_style)]
        ]
        emp_table = Table(emp_data, colWidths=[150, 350])
        emp_table.setStyle(TableStyle([
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
            ('PADDING', (0,0), (-1,-1), 6),
            ('BACKGROUND', (0,0), (0,-1), colors.HexColor("#f8fafc")),
        ]))
        story.append(emp_table)
        story.append(Spacer(1, 20))

        story.append(Paragraph("Salary Breakdown", header_style))
        breakdown_data = [
            [Paragraph("<b>Item Description</b>", body_style), Paragraph("<b>Earnings (+)</b>", body_style), Paragraph("<b>Deductions (-)</b>", body_style)],
            [Paragraph("Base Salary", body_style), Paragraph(f"${detail.base_salary:,.2f}", body_style), Paragraph("$0.00", body_style)],
            [Paragraph("Bonus Reward", body_style), Paragraph(f"${detail.bonus:,.2f}", body_style), Paragraph("$0.00", body_style)],
            [Paragraph("Commission Earned", body_style), Paragraph(f"${detail.commission:,.2f}", body_style), Paragraph("$0.00", body_style)],
            [Paragraph("Overtime Pay", body_style), Paragraph(f"${detail.overtime:,.2f}", body_style), Paragraph("$0.00", body_style)],
            [Paragraph("Absence Penalty", body_style), Paragraph("$0.00", body_style), Paragraph(f"${detail.absence_deduction:,.2f}", body_style)],
            [Paragraph("Late Penalty", body_style), Paragraph("$0.00", body_style), Paragraph(f"${detail.late_deduction:,.2f}", body_style)],
            [Paragraph("Loan Repayments", body_style), Paragraph("$0.00", body_style), Paragraph(f"${detail.loan_deduction:,.2f}", body_style)],
            [Paragraph("<b>Net Salary Paid</b>", body_style), Paragraph(f"<b>${detail.net_salary:,.2f}</b>", body_style), Paragraph("", body_style)]
        ]
        
        breakdown_table = Table(breakdown_data, colWidths=[200, 150, 150])
        breakdown_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
            ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor("#eff6ff")), # highlight net salary
            ('LINEBELOW', (0,-1), (-1,-1), 1.5, colors.HexColor("#2563eb")),
            ('PADDING', (0,0), (-1,-1), 8),
        ]))
        story.append(breakdown_table)

        # Build Document
        doc.build(story)
        
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response
