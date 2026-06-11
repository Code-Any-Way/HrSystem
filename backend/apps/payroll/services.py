import calendar
from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from employees.models import Employee
from attendance.models import Attendance, AttendanceStatus
from payroll.models import PayrollRun, PayrollDetail, PayrollRunStatus

class PayrollService:
    @staticmethod
    @transaction.atomic
    def generate_monthly_payroll(company, month, year):
        """
        Service method to calculate monthly payroll for all active employees
        in a company, factoring in lateness and absences.
        """
        # 1. Create or fetch Draft Payroll Run
        payroll_run, created = PayrollRun.objects.get_or_create(
            company=company,
            month=month,
            year=year,
            defaults={'status': PayrollRunStatus.DRAFT}
        )

        if payroll_run.status != PayrollRunStatus.DRAFT:
            raise ValueError("Payroll run for this period is already approved or paid.")

        # 2. Get active employees
        employees = Employee.objects.filter(
            branch__company=company,
            status='ACTIVE'
        )

        # 3. Calculate calendar details
        num_days = calendar.monthrange(year, month)[1]
        start_date = timezone.datetime(year, month, 1).date()
        end_date = timezone.datetime(year, month, num_days).date()

        generated_details = []

        for emp in employees:
            base = emp.base_salary
            daily_rate = base / Decimal(30.0)  # Standard month billing days
            
            # Count attendance metrics for this period
            attendances = Attendance.objects.filter(
                employee=emp,
                date__range=(start_date, end_date)
            )
            
            absent_count = attendances.filter(status=AttendanceStatus.ABSENT).count()
            late_count = attendances.filter(status=AttendanceStatus.LATE).count()
            
            # Formulate deductions:
            # Absence deduction = daily rate * absent days
            absence_deduction = daily_rate * Decimal(absent_count)
            # Late deduction = daily rate / 8 (approx 1 hr pay penalty per lateness) * late days
            late_deduction = (daily_rate / Decimal(8.0)) * Decimal(late_count)
            
            # Calculate default overtime, commission, bonus (can be updated later by HR)
            bonus = Decimal(0.0)
            commission = Decimal(0.0)
            overtime = Decimal(0.0)
            loan_deduction = Decimal(0.0)
            
            # Update or create the payroll detail for employee
            detail, _ = PayrollDetail.objects.update_or_create(
                payroll_run=payroll_run,
                employee=emp,
                defaults={
                    'base_salary': base,
                    'bonus': bonus,
                    'commission': commission,
                    'overtime': overtime,
                    'absence_deduction': absence_deduction.quantize(Decimal('0.01')),
                    'late_deduction': late_deduction.quantize(Decimal('0.01')),
                    'loan_deduction': loan_deduction,
                }
            )
            generated_details.append(detail)
            
        return payroll_run, generated_details
