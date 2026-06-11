# Django Admin Panel Guide

## Default Login Credentials

**Admin User:**
- Username: `admin`
- Password: `admin123`
- Email: `admin@techsolutions.com`

**Sample Employee Accounts:**
1. Username: `EMP001` | Password: `employee123` (John Developer)
2. Username: `EMP002` | Password: `employee123` (Jane Manager)
3. Username: `EMP003` | Password: `employee123` (Mike Designer)

## Accessing the Admin Panel

1. Start the Django development server:
```bash
python manage.py runserver
```

2. Navigate to: `http://localhost:8000/admin/`

3. Login with admin credentials

## Admin Panel Features

### 1. **User Management** (`/admin/accounts/user/`)
- View all users in the system
- Manage user roles (Super Admin, Company Admin, HR Manager, Manager, Employee)
- Assign company and branch associations
- View user permissions and groups
- Filter by role, company, branch, staff status, or superuser status

### 2. **Permissions & Groups** (`/admin/auth/`)
- **Groups** (`/admin/auth/group/`): Manage user groups (Super Admin, Company Admin, HR Manager, Manager, Employee)
- **Permissions** (`/admin/auth/permission/`): View all system permissions organized by content type

### 3. **Company Management**
- **Companies** (`/admin/companies/company/`):
  - View all companies
  - See branch count and department count for each company
  - Filter by creation date
  - Search by name, email, phone, or address

- **Branches** (`/admin/companies/branch/`):
  - View all branches with their company association
  - See employee count for each branch
  - Filter by company and creation date
  - Search by name, email, phone, or address

### 4. **Organization Structure**
- **Departments** (`/admin/departments/department/`):
  - Manage company departments
  - View department descriptions
  - Filter by company and creation date
  - Full text search

- **Teams** (`/admin/teams/team/`):
  - Manage department teams
  - Assign team leaders
  - Filter by department and company
  - View creation/update timestamps

### 5. **Employee Management**
- **Employees** (`/admin/employees/employee/`):
  - Complete employee records with:
    - Personal info (name, email, phone, DoB, gender, national ID)
    - Employment details (job title, department, team, branch, manager)
    - Contract info (hire date, base salary, employment type, status)
  - Filter by status, employment type, department, branch, team, or hire date
  - Date hierarchy view by hire date
  - Full search capability

### 6. **Attendance & Time Tracking**
- **Attendance** (`/admin/attendance/attendance/`):
  - Track employee attendance records
  - Log check-in/check-out times
  - Record attendance status (Present, Absent, Late, Leave, Holiday)
  - GPS coordinates for check-in/out locations (latitude/longitude)
  - IP address logging
  - QR token verification records
  - Date hierarchy view
  - Filter by status, date, department, or branch

### 7. **Leave Management**
- **Leave Requests** (`/admin/leaves/leaverequest/`):
  - View all leave requests
  - Display leave duration in days
  - Track approval workflow (manager → HR)
  - Show approval dates and personnel
  - Rejection reasons
  - Leave types: Annual, Sick, Emergency, Unpaid
  - Status tracking through workflow

### 8. **Asset Management**
- **Assets** (`/admin/assets/asset/`):
  - Track company assets (Laptop, Phone, SIM Card, Vehicle, Other)
  - Serial number tracking
  - Asset status (Available, Assigned, Under Repair, Retired)
  - View current assignee

- **Asset Assignments** (`/admin/assets/assetassignment/`):
  - Track asset assignment history
  - Record assignment/return dates
  - Condition notes on assignment and return
  - Complete assignment timeline

### 9. **Payroll & Compensation**
- **Payroll Runs** (`/admin/payroll/payrollrun/`):
  - Create and manage monthly payroll runs
  - Track payroll status (Draft, Approved, Paid)
  - Filter by status, year, month, and company
  - View employee count in each payroll run

- **Payroll Details** (`/admin/payroll/payrolldetail/`):
  - Detailed salary breakdown per employee
  - Components: Base salary, bonus, commission, overtime
  - Deductions: Absence, late, loan
  - Auto-calculated net salary
  - Filter by payroll run and employee department

### 10. **Expense Management**
- **Expense Requests** (`/admin/expenses/expenserequest/`):
  - Track employee expense claims
  - Categories: Travel, Meals, Supplies, Utilities, Other
  - Approval workflow (Manager → Finance)
  - Receipt file attachments
  - Rejection reason tracking
  - Status: Pending Manager, Pending Finance, Approved, Rejected

### 11. **Performance Evaluation**
- **Performance Evaluations** (`/admin/evaluations/performanceevaluation/`):
  - Track employee performance scores (1-100)
  - Evaluation periods (e.g., Q1 2026, Annual 2025)
  - Evaluator assignment
  - Evaluation notes
  - Unique evaluations per employee per period

### 12. **Notifications**
- **Notifications** (`/admin/notifications/notification/`):
  - System notifications for all users
  - Types: Info, Warning, Success, Danger
  - Read status tracking
  - User-specific filtering
  - Read-only admin (auto-created)

### 13. **Audit Logs**
- **Audit Logs** (`/admin/audit_logs/auditlog/`):
  - Complete system audit trail
  - Action tracking: CREATE, UPDATE, DELETE, LOGIN, LOGOUT
  - User, model name, and object ID logging
  - Old and new data comparison (JSON format)
  - IP address logging
  - Date hierarchy
  - Read-only and protected (no deletion allowed)

## Default Data Structure

### Created Companies:
1. **Tech Solutions Inc**
   - Main Branch & Secondary Branch
   - Departments: Engineering, Human Resources, Finance
   - Teams: Backend Team, Frontend Team (under Engineering), Recruitment (under HR)

2. **Global Innovations Ltd**
   - Main Branch & Secondary Branch
   - Departments: Sales, Marketing
   - Teams: Enterprise Sales (under Sales)

### Created Permission Groups:
- Super Admin
- Company Admin
- HR Manager
- Manager
- Employee

### Sample Employees:
- EMP001: John Developer - Senior Developer (Engineering)
- EMP002: Jane Manager - Project Manager (Human Resources)
- EMP003: Mike Designer - UI/UX Designer (Engineering)

## Admin Features

### Search Capabilities
All models support comprehensive search across relevant fields:
- Employees: Search by code, name, email
- Attendance: Search by employee code, name, IP address
- Leave Requests: Search by employee, reason
- Expense Requests: Search by title, description, employee name
- Assets: Search by name, serial number, company
- And more...

### Filtering Options
Every model includes intelligent filters:
- Status-based filters
- Date range filters
- Department/Company hierarchical filters
- Role-based filters
- And context-specific filters

### Date Hierarchy
Models with date fields include date hierarchy navigation:
- Attendance: Navigate by date
- Leave Requests: Navigate by start date
- Payroll: Navigate by salary month
- Evaluations: Navigate by creation date
- Notifications: Navigate by creation date

### Read-Only Fields
Audit logs and notifications are protected:
- Cannot manually add entries (auto-created)
- Audit logs cannot be deleted (immutable)
- View-only access to critical system data

## Tips & Best Practices

1. **Permissions & Groups**: Assign users to groups for role-based access control
2. **Audit Trail**: Check audit logs for system changes and user activities
3. **Attendance**: Use GPS coordinates for location-based check-in validation
4. **Approval Workflow**: Respect the multi-level approval workflow for leaves and expenses
5. **Asset Tracking**: Keep asset serial numbers up-to-date for inventory management
6. **Payroll**: Draft payroll first, review, then approve before payment
7. **Performance Reviews**: Set specific evaluation periods for consistency

## Customization

To customize the admin panel further:

1. Edit relevant `admin.py` files in each app
2. Modify `list_display`, `list_filter`, `search_fields`, `fieldsets`
3. Add custom actions or methods to admin classes
4. Restart Django development server

Example:
```python
# In apps/employees/admin.py
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_code', 'first_name', 'last_name', 'email', ...)
    list_filter = ('status', 'department', ...)
    search_fields = ('employee_code', 'first_name', ...)
```

## Troubleshooting

**Issue**: Cannot login to admin panel
- Verify credentials match the defaults above
- Check if database has been migrated: `python manage.py migrate`
- Check if default data has been created: `python manage.py create_default_data`

**Issue**: Missing models in admin
- Ensure models are registered in `admin.py`
- Verify app is in `INSTALLED_APPS` in settings.py
- Restart Django server

**Issue**: Permissions not working
- Verify user is assigned to correct group
- Check group permissions are properly configured
- Review permission model in admin panel

---

**Last Updated**: 2026-06-11
**Django Version**: 5.0+
**DRF Version**: 3.15+
