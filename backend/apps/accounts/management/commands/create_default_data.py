from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from accounts.models import User
from companies.models import Company, Branch
from departments.models import Department
from teams.models import Team
from employees.models import Employee


class Command(BaseCommand):
    help = 'Create default data including companies, departments, teams, employees, and permissions'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting default data creation...'))

        # Create Permission Groups
        self.create_permission_groups()

        # Create Companies and Branches
        companies_data = self.create_companies()

        # Create Departments
        departments_data = self.create_departments(companies_data)

        # Create Teams
        self.create_teams(departments_data)

        # Create Admin User
        self.create_admin_user(companies_data)

        # Create Sample Employees
        self.create_sample_employees(companies_data, departments_data)

        self.stdout.write(self.style.SUCCESS('Default data creation completed successfully!'))

    def create_permission_groups(self):
        """Create default permission groups"""
        self.stdout.write('Creating permission groups...')

        groups_names = ['Super Admin', 'Company Admin', 'HR Manager', 'Manager', 'Employee']

        for group_name in groups_names:
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(f'  Created group: {group_name}')

    def create_companies(self):
        """Create default companies"""
        self.stdout.write('Creating companies...')

        companies = [
            {
                'name': 'Tech Solutions Inc',
                'email': 'contact@techsolutions.com',
                'phone': '+1-555-0100',
                'address': '123 Tech Street, Silicon Valley, CA 94025',
            },
            {
                'name': 'Global Innovations Ltd',
                'email': 'info@globalinnovations.com',
                'phone': '+1-555-0200',
                'address': '456 Innovation Ave, New York, NY 10001',
            },
        ]

        companies_dict = {}
        for company_data in companies:
            company, created = Company.objects.get_or_create(
                name=company_data['name'],
                defaults={
                    'email': company_data['email'],
                    'phone': company_data['phone'],
                    'address': company_data['address'],
                }
            )
            if created:
                self.stdout.write(f'  Created company: {company.name}')
            companies_dict[company.name] = company

            # Create branches for each company
            branches = [
                {
                    'name': f'{company.name} - Main Branch',
                    'email': f'main@{company.email.split("@")[1]}',
                    'phone': company.phone,
                    'address': company.address,
                },
                {
                    'name': f'{company.name} - Secondary Branch',
                    'email': f'secondary@{company.email.split("@")[1]}',
                    'phone': company.phone,
                    'address': f'{company.address} (Branch 2)',
                },
            ]

            for branch_data in branches:
                branch, created = Branch.objects.get_or_create(
                    company=company,
                    name=branch_data['name'],
                    defaults={
                        'email': branch_data['email'],
                        'phone': branch_data['phone'],
                        'address': branch_data['address'],
                    }
                )
                if created:
                    self.stdout.write(f'    Created branch: {branch.name}')

        return companies_dict

    def create_departments(self, companies_dict):
        """Create default departments"""
        self.stdout.write('Creating departments...')

        departments_dict = {}
        departments_data = [
            {'company': 'Tech Solutions Inc', 'name': 'Engineering', 'description': 'Software Development'},
            {'company': 'Tech Solutions Inc', 'name': 'Human Resources', 'description': 'HR & Recruitment'},
            {'company': 'Tech Solutions Inc', 'name': 'Finance', 'description': 'Finance & Accounting'},
            {'company': 'Global Innovations Ltd', 'name': 'Sales', 'description': 'Sales & Business Development'},
            {'company': 'Global Innovations Ltd', 'name': 'Marketing', 'description': 'Marketing & Communications'},
        ]

        for dept_data in departments_data:
            company = companies_dict.get(dept_data['company'])
            if company:
                dept, created = Department.objects.get_or_create(
                    company=company,
                    name=dept_data['name'],
                    defaults={'description': dept_data['description']}
                )
                if created:
                    self.stdout.write(f'  Created department: {dept.name}')
                departments_dict[f"{company.name}:{dept.name}"] = dept

        return departments_dict

    def create_teams(self, departments_dict):
        """Create default teams"""
        self.stdout.write('Creating teams...')

        teams_data = [
            {'dept_key': 'Tech Solutions Inc:Engineering', 'name': 'Backend Team'},
            {'dept_key': 'Tech Solutions Inc:Engineering', 'name': 'Frontend Team'},
            {'dept_key': 'Tech Solutions Inc:Human Resources', 'name': 'Recruitment'},
            {'dept_key': 'Global Innovations Ltd:Sales', 'name': 'Enterprise Sales'},
        ]

        for team_data in teams_data:
            dept = departments_dict.get(team_data['dept_key'])
            if dept:
                team, created = Team.objects.get_or_create(
                    department=dept,
                    name=team_data['name'],
                )
                if created:
                    self.stdout.write(f'  Created team: {team.name}')

    def create_admin_user(self, companies_dict):
        """Create admin user"""
        self.stdout.write('Creating admin user...')

        tech_company = list(companies_dict.values())[0]
        main_branch = tech_company.branches.first()

        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@techsolutions.com',
                'first_name': 'Admin',
                'last_name': 'User',
                'role': 'SUPER_ADMIN',
                'company': tech_company,
                'branch': main_branch,
                'is_staff': True,
                'is_superuser': True,
                'is_active': True,
            }
        )

        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(f'  Created admin user: {admin_user.username}')

        # Add admin to Super Admin group
        super_admin_group, _ = Group.objects.get_or_create(name='Super Admin')
        admin_user.groups.add(super_admin_group)

    def create_sample_employees(self, companies_dict, departments_dict):
        """Create sample employees"""
        self.stdout.write('Creating sample employees...')

        tech_company = list(companies_dict.values())[0]
        main_branch = tech_company.branches.first()

        employees_data = [
            {
                'employee_code': 'EMP001',
                'first_name': 'John',
                'last_name': 'Developer',
                'email': 'john.developer@techsolutions.com',
                'job_title': 'Senior Developer',
                'dept_key': 'Tech Solutions Inc:Engineering',
                'user_email': 'john.dev@techsolutions.com',
            },
            {
                'employee_code': 'EMP002',
                'first_name': 'Jane',
                'last_name': 'Manager',
                'email': 'jane.manager@techsolutions.com',
                'job_title': 'Project Manager',
                'dept_key': 'Tech Solutions Inc:Human Resources',
                'user_email': 'jane.mgr@techsolutions.com',
            },
            {
                'employee_code': 'EMP003',
                'first_name': 'Mike',
                'last_name': 'Designer',
                'email': 'mike.designer@techsolutions.com',
                'job_title': 'UI/UX Designer',
                'dept_key': 'Tech Solutions Inc:Engineering',
                'user_email': 'mike.designer@techsolutions.com',
            },
        ]

        for emp_data in employees_data:
            dept = departments_dict.get(emp_data['dept_key'])
            if dept:
                # Create user account for employee
                user, user_created = User.objects.get_or_create(
                    username=emp_data['employee_code'],
                    defaults={
                        'email': emp_data['user_email'],
                        'first_name': emp_data['first_name'],
                        'last_name': emp_data['last_name'],
                        'role': 'EMPLOYEE',
                        'company': tech_company,
                        'branch': main_branch,
                        'is_active': True,
                    }
                )

                if user_created:
                    user.set_password('employee123')
                    user.save()

                # Create employee record
                employee, created = Employee.objects.get_or_create(
                    employee_code=emp_data['employee_code'],
                    defaults={
                        'user': user,
                        'first_name': emp_data['first_name'],
                        'last_name': emp_data['last_name'],
                        'email': emp_data['email'],
                        'job_title': emp_data['job_title'],
                        'department': dept,
                        'branch': main_branch,
                        'status': 'ACTIVE',
                        'employment_type': 'FULL_TIME',
                        'hire_date': __import__('datetime').date.today(),
                        'base_salary': 50000.00,
                    }
                )

                if created:
                    self.stdout.write(f'  Created employee: {employee.employee_code} - {employee.first_name} {employee.last_name}')
