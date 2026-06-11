import { defineStore } from 'pinia'
import { login as loginService, fetchProfile } from '../services/auth'

interface UserProfile {
  id: string
  email: string
  first_name: string
  last_name: string
  role: string
}

interface RoleDefinition {
  id: string
  name: {
    en: string
    ar: string
  }
}

const translations = {
  en: {
    navHome: 'Home',
    navDashboard: 'Dashboard',
    navEmployees: 'Employees',
    navAttendance: 'Attendance',
    navLeaves: 'Leaves',
    navPayroll: 'Payroll',
    navAssets: 'Assets',
    navExpenses: 'Expenses',
    navEvaluations: 'Evaluations',
    navSettings: 'Settings',
    navLogin: 'Login',
    navLogout: 'Logout',
    themeLight: 'Light mode',
    themeDark: 'Dark mode',
    language: 'Language',
    overviewLabel: 'HRMS Overview',
    homepageHeadline: 'A modern HR experience for every team',
    homepageSubtitle: 'Build a connected company culture, manage people, payroll, attendance and analytics in one place.',
    homepageButton: 'Explore the control panel',
    companyMission: 'We help teams stay productive with fast people operations, secure payroll, and data-driven insights.',
    featureOne: 'Unified employee directory and role management.',
    featureTwo: 'Attendance tracking, leave workflows, and approvals.',
    featureThree: 'Financial reporting, payroll runs, expenses, and asset control.',
    adminHeaderSubtitle: 'Human Resource Management',
    adminHeaderTitle: 'Central Command Center',
    adminStatusBadge: 'Admin dashboard ready',
    sectionEmployeeManagement: 'Employee Management',
    sectionEmployeeManagementText: 'Browse staff, profiles, departments, and branch assignment.',
    sectionAttendance: 'Attendance',
    sectionAttendanceText: 'Monitor check-ins, GPS logs, and daily status reports.',
    sectionPayroll: 'Payroll',
    sectionPayrollText: 'Review salary runs, deductions, and net pay with confidence.',
    sectionLeaveManagement: 'Leave Management',
    sectionLeaveManagementText: 'Manage approvals, balances, and leave workflows in one place.',
    sectionAssets: 'Assets',
    sectionAssetsText: 'Track inventory, assignments, and asset conditions.',
    sectionNotifications: 'Notifications',
    sectionNotificationsText: 'Stay updated with alerts, system notices, and workflow reminders.',
    dashboardAttendanceAnalytics: 'Attendance analytics',
    dashboardAttendanceAnalyticsText: 'Weekly attendance rate and check-in stability.',
    dashboardLiveTag: 'Live',
    dashboardDepartmentPerformance: 'Department performance',
    dashboardDepartmentPerformanceText: 'Current team distribution and workload share.',
    dashboardInsightTag: 'Insight',
    dashboardSummaryLabel: 'Executive summary',
    dashboardSummaryTitle: 'Operational health at a glance',
    dashboardSummarySubtitle: 'Track recent activity, approvals pending, and department performance across your HR ecosystem.',
    dashboardRefreshOverview: 'Refresh overview',
    dashboardEmployeesLabel: 'Employees',
    dashboardEmployeesText: 'Active staff across all branches.',
    dashboardAttendanceLabel: 'Attendance',
    dashboardAttendanceText: 'This week’s on-time check-ins.',
    dashboardPendingLeavesLabel: 'Pending leaves',
    dashboardPendingLeavesText: 'Awaiting manager approval.',
    dashboardPayrollRunsLabel: 'Payroll runs',
    dashboardPayrollRunsText: 'Payments queued for processing.',
    dashboardTeamPulseTitle: 'Team pulse',
    dashboardPulseSubtitle: 'Keep track of employee engagement, approval times, and payroll readiness.',
    dashboardAttendanceHighlightsTitle: 'Attendance highlights',
    dashboardAttendanceHighlightsSubtitle: 'Recent events and status updates from today’s attendance data.',
    dashboardRecentApprovals: 'Recent approvals',
    dashboardLeaveRequest: 'Leave request',
    dashboardExpenseClaim: 'Expense claim',
    dashboardAssetReturn: 'Asset return',
    attendanceTrendTitle: 'Weekly attendance trend',
    departmentChartTitle: 'Team distribution',
    attendanceSeriesLabel: 'Attendance %',
    loginTitle: 'Secure HRMS Access',
    loginSubtitle: 'Sign in securely to manage employees, requests, payroll, attendance and more.',
    loginButton: 'Sign in',
    loginError: 'Login failed. Check your credentials and try again.',
    loginEmailLabel: 'Email address',
    loginPasswordLabel: 'Password',
    loginEmailPlaceholder: 'name@company.com',
    loginPasswordPlaceholder: '••••••••',
    controlPanel: 'Control panel',
    rolePanelDescriptionSuperAdmin: 'Manage company-wide operations, user roles, and analytics from one place.',
    rolePanelDescriptionManager: 'Oversee your team, review approvals, and keep projects on track.',
    rolePanelDescriptionHR: 'Handle HR workflows, payroll, leave approvals, and employee records.',
    rolePanelDescriptionEmployee: 'View your personal attendance, leave status, and payroll information.',
    roleCardEmployees: 'Employees',
    roleCardAttendance: 'Attendance',
    roleCardPending: 'Pending approvals',
    roleCardPayroll: 'Payroll schedule',
    roleCardLeaveBalance: 'Leave balance',
    roleCardAssets: 'Assigned assets',
    mainHeadline: 'All your HR data in one place',
    mainDescription: 'Quickly access employees, attendance, payroll, leave requests, assets, expenses, and evaluations from a single unified workspace.',
    employeesTitle: 'Employee roster',
    employeesSubtitle: 'Review current staff details and branch assignments.',
    employeesRefresh: 'Refresh list',
    employeesTotal: 'Total staff',
    employeesDepartments: 'Departments',
    employeesRecentHire: 'New this month',
    employeesRecords: 'Employee records',
    employeesUpdated: 'Updated just now',
    employeesNoData: 'No employees found yet.',
    attendanceTitle: 'Daily presence and check-in analytics',
    attendanceSync: 'Sync attendance',
    attendanceSubtitle: 'Monitor real-time attendance, GPS check-in trends, and employee presence in one easy view.',
    attendancePresent: 'Today present',
    attendanceLate: 'Late arrivals',
    attendanceAbsent: 'Absent',
    attendanceGps: 'GPS checks',
    attendanceHighlights: 'Attendance highlights',
    leavesTitle: 'Leave requests and balance tracking',
    leavesSubtitle: 'Review all leave requests, approval history, and remaining balance across teams.',
    leavesPending: 'Pending',
    leavesApproved: 'Approved',
    leavesDeclined: 'Declined',
    leavesBalance: 'Available balance',
    payrollTitle: 'Pay runs, deductions, and approvals',
    payrollSubtitle: 'Manage payroll cycles, review payroll summaries, and confirm deposits for upcoming salary payments.',
    payrollNext: 'Next payroll',
    payrollTotalNet: 'Total net',
    payrollPending: 'Pending approvals',
    payrollDeductions: 'Deductions',
    payrollSummary: 'Payroll summary',
    assetsTitle: 'Inventory and assignment tracking',
    assetsSubtitle: 'Keep asset inventory up to date and monitor which devices are assigned to employees.',
    assetsTotal: 'Total assets',
    assetsAssigned: 'Assigned',
    assetsDue: 'Due returns',
    assetsAlerts: 'Condition alerts',
    expensesTitle: 'Claims review and reimbursement tracking',
    expensesSubtitle: 'Manage expense approvals, outstanding reimbursements, and claim history across departments.',
    expensesPending: 'Pending',
    expensesPaid: 'Paid',
    expensesTotal: 'Total reimbursement',
    expensesPriority: 'High priority',
    evaluationsTitle: 'Performance reviews and outcome tracking',
    evaluationsSubtitle: 'Monitor employee performance cycles, goal completion, and feedback from across the organization.',
    evaluationsActive: 'Active reviews',
    evaluationsCompleted: 'Completed',
    evaluationsFeedback: 'Pending feedback',
    evaluationsGoals: 'Goals aligned',
    settingsTitle: 'Settings',
    settingsProfile: 'Profile settings',
    settingsSystem: 'System preferences',
    settingsProfileText: 'Update your name, email, and contact information.',
    settingsSystemText: 'Manage notifications, language, and accessibility settings.',
    editProfile: 'Edit profile',
    changePassword: 'Change password',
    notificationPrefs: 'Notification preferences',
    themeLayout: 'Theme and layout',
    roleManagement: 'Role management',
    roleManagementText: 'Create and edit roles used across the control panel.',
    addRole: 'Add new role',
    roleNameEn: 'Role name (English)',
    roleNameAr: 'Role name (Arabic)',
    saveRole: 'Save role',
    noRoles: 'No custom roles defined yet.',
    role: 'Role',
    roleAssigned: 'Assigned role',
    selectRole: 'Select role',
  },
  ar: {
    navHome: 'الرئيسية',
    navDashboard: 'لوحة البيانات',
    navEmployees: 'الموظفون',
    navAttendance: 'الحضور',
    navLeaves: 'الإجازات',
    navPayroll: 'الرواتب',
    navAssets: 'الأصول',
    navExpenses: 'المصاريف',
    navEvaluations: 'التقييمات',
    navSettings: 'الإعدادات',
    navLogin: 'تسجيل الدخول',
    navLogout: 'تسجيل الخروج',
    themeLight: 'الوضع الفاتح',
    themeDark: 'الوضع الداكن',
    language: 'اللغة',
    overviewLabel: 'نظرة عامة على الموارد البشرية',
    homepageHeadline: 'تجربة موارد بشرية حديثة لكل الفرق',
    homepageSubtitle: 'إدارة الموظفين والرواتب والحضور والتحليلات من مكان واحد.',
    homepageButton: 'استعراض لوحة التحكم',
    companyMission: 'نساعد الفرق على البقاء منتجة من خلال عمليات موظفين سريعة، رواتب آمنة، ورؤى مدعومة بالبيانات.',
    featureOne: 'دليل موظفين موحد وإدارة الأدوار.',
    featureTwo: 'تتبع الحضور وسير عمل الإجازات والموافقات.',
    featureThree: 'تقارير مالية، دفعات رواتب، مصاريف، وتحكم في الأصول.',
    adminHeaderSubtitle: 'إدارة الموارد البشرية',
    adminHeaderTitle: 'مركز القيادة المركزي',
    adminStatusBadge: 'لوحة الإدارة جاهزة',
    sectionEmployeeManagement: 'إدارة الموظفين',
    sectionEmployeeManagementText: 'استعرض الموظفين، الملفات الشخصية، الأقسام، وتوزيع الفروع.',
    sectionAttendance: 'الحضور',
    sectionAttendanceText: 'تابع تسجيلات الحضور، GPS، وتقرير الحالة اليومية.',
    sectionPayroll: 'الرواتب',
    sectionPayrollText: 'راجع دورات الرواتب، الخصومات، وصافي الأجور بثقة.',
    sectionLeaveManagement: 'إدارة الإجازات',
    sectionLeaveManagementText: 'أدر الموافقات، الأرصدة، وسير عمل الإجازات في مكان واحد.',
    sectionAssets: 'الأصول',
    sectionAssetsText: 'تتبع المخزون، التعيينات، وحالة الأصول.',
    sectionNotifications: 'الإشعارات',
    sectionNotificationsText: 'ابقَ محدثًا بالتنبيهات والإشعارات ونذكيرات سير العمل.',
    dashboardAttendanceAnalytics: 'تحليلات الحضور',
    dashboardAttendanceAnalyticsText: 'نسبة الحضور الأسبوعية واستقرار تسجيلات الدخول.',
    dashboardLiveTag: 'مباشر',
    dashboardDepartmentPerformance: 'أداء الأقسام',
    dashboardDepartmentPerformanceText: 'توزيع الفريق الحالي وحصة عبء العمل.',
    dashboardInsightTag: 'رؤى',
    dashboardSummaryLabel: 'الملخص التنفيذي',
    dashboardSummaryTitle: 'الصحة التشغيلية بنظرة سريعة',
    dashboardSummarySubtitle: 'تابع النشاط الأخير والموافقات المعلقة وأداء الأقسام عبر نظام الموارد البشرية الخاص بك.',
    dashboardRefreshOverview: 'تحديث النظرة العامة',
    dashboardEmployeesLabel: 'الموظفون',
    dashboardEmployeesText: 'الموظفون النشطون عبر جميع الفروع.',
    dashboardAttendanceLabel: 'الحضور',
    dashboardAttendanceText: 'دقة تسجيل الوصول في الوقت المحدد لهذا الأسبوع.',
    dashboardPendingLeavesLabel: 'الإجازات المعلقة',
    dashboardPendingLeavesText: 'بانتظار موافقة المدير.',
    dashboardPayrollRunsLabel: 'دورات الرواتب',
    dashboardPayrollRunsText: 'المدفوعات المقررة للمعالجة.',
    dashboardTeamPulseTitle: 'نبض الفريق',
    dashboardPulseSubtitle: 'تابع تفاعل الموظفين وأوقات الموافقة واستعداد الرواتب.',
    dashboardAttendanceHighlightsTitle: 'أهم نقاط الحضور',
    dashboardAttendanceHighlightsSubtitle: 'الأحداث الحديثة وتحديثات الحالة من بيانات الحضور اليوم.',
    dashboardRecentApprovals: 'الموافقات الأخيرة',
    dashboardLeaveRequest: 'طلب إجازة',
    dashboardExpenseClaim: 'مطالبة مصاريف',
    dashboardAssetReturn: 'إعادة أصل',
    attendanceTrendTitle: 'اتجاه الحضور الأسبوعي',
    departmentChartTitle: 'توزيع الفريق',
    attendanceSeriesLabel: 'نسبة الحضور',
    loginTitle: 'دخول آمن إلى النظام',
    loginSubtitle: 'سجّل الدخول لإدارة الموظفين والطلبات والرواتب والحضور والمزيد.',
    loginButton: 'تسجيل الدخول',
    loginError: 'فشل تسجيل الدخول. تحقق من بياناتك وحاول مرة أخرى.',
    loginEmailLabel: 'البريد الإلكتروني',
    loginPasswordLabel: 'كلمة المرور',
    loginEmailPlaceholder: 'name@company.com',
    loginPasswordPlaceholder: '••••••••',
    controlPanel: 'لوحة التحكم',
    rolePanelDescriptionSuperAdmin: 'أدر عمليات الشركة، الأدوار، والتحليلات من مكان واحد.',
    rolePanelDescriptionManager: 'اشرف على فريقك، راجع الموافقات، واحفظ المشاريع في المسار الصحيح.',
    rolePanelDescriptionHR: 'تعامل مع سير عمل الموارد البشرية، الرواتب، الموافقات، وسجلات الموظفين.',
    rolePanelDescriptionEmployee: 'اعرض حضورك الشخصي، حالة الإجازة، ومعلومات الرواتب.',
    roleCardEmployees: 'الموظفون',
    roleCardAttendance: 'الحضور',
    roleCardPending: 'الموافقات المعلقة',
    roleCardPayroll: 'جدول الرواتب',
    roleCardLeaveBalance: 'رصيد الإجازات',
    roleCardAssets: 'الأصول المعينة',
    mainHeadline: 'جميع بيانات الموارد البشرية في مكان واحد',
    mainDescription: 'الوصول السريع إلى الموظفين، الحضور، الرواتب، طلبات الإجازة، الأصول، المصاريف، والتقييمات.',
    employeesTitle: 'قائمة الموظفين',
    employeesSubtitle: 'استعرض تفاصيل الموظفين الحالية وتوزيع الفروع.',
    employeesRefresh: 'تحديث القائمة',
    employeesTotal: 'إجمالي الموظفين',
    employeesDepartments: 'الأقسام',
    employeesRecentHire: 'جدد هذا الشهر',
    employeesRecords: 'سجلات الموظفين',
    employeesUpdated: 'تم التحديث الآن',
    employeesNoData: 'لا يوجد موظفين حتى الآن.',
    attendanceTitle: 'تحليلات الحضور وتسجيلات الانصراف',
    attendanceSync: 'مزامنة الحضور',
    attendanceSubtitle: 'تابع الحضور في الوقت الحقيقي واتجاهات التحقق بالموقع بسهولة.',
    attendancePresent: 'حاضر اليوم',
    attendanceLate: 'الوصول المتأخر',
    attendanceAbsent: 'غياب',
    attendanceGps: 'التحقق بالموقع',
    attendanceHighlights: 'أهم نقاط الحضور',
    leavesTitle: 'طلبات الإجازة وتتبع الرصيد',
    leavesSubtitle: 'راجع جميع الطلبات وسجل الموافقات والرصيد المتبقي.',
    leavesPending: 'قيد الانتظار',
    leavesApproved: 'الموافق عليها',
    leavesDeclined: 'المرفوضة',
    leavesBalance: 'الرصيد المتاح',
    payrollTitle: 'دفعات الرواتب والخصومات والموافقات',
    payrollSubtitle: 'إدارة دورات الرواتب ومراجعة الملخصات وتأكيد الإيداعات.',
    payrollNext: 'الرواتب القادمة',
    payrollTotalNet: 'صافي الإجمالي',
    payrollPending: 'موافقات معلقة',
    payrollDeductions: 'الخصومات',
    payrollSummary: 'ملخص الرواتب',
    assetsTitle: 'تتبع الأصول والتوزيع',
    assetsSubtitle: 'حافظ على مخزون الأصول وتعرّف على الأجهزة المعينة للموظفين.',
    assetsTotal: 'إجمالي الأصول',
    assetsAssigned: 'المُسندة',
    assetsDue: 'العائدات القادمة',
    assetsAlerts: 'تنبيهات الحالة',
    expensesTitle: 'مراجعة المصاريف وتتبع التعويضات',
    expensesSubtitle: 'إدارة الموافقات، المبالغ المستحقة، وسجل المطالبات.',
    expensesPending: 'قيد الانتظار',
    expensesPaid: 'تم الدفع',
    expensesTotal: 'إجمالي التعويضات',
    expensesPriority: 'أولوية عالية',
    evaluationsTitle: 'التقييمات وتتبع النتائج',
    evaluationsSubtitle: 'راقب دورات الأداء وإكمال الأهداف والتعليقات.',
    evaluationsActive: 'التقييمات النشطة',
    evaluationsCompleted: 'المكتملة',
    evaluationsFeedback: 'التعليقات المعلقة',
    evaluationsGoals: 'الأهداف المحققة',
    settingsTitle: 'الإعدادات',
    settingsProfile: 'إعدادات الملف الشخصي',
    settingsSystem: 'تفضيلات النظام',
    settingsProfileText: 'حدِّث اسمك والبريد الإلكتروني ومعلومات الاتصال.',
    settingsSystemText: 'أدِر الإشعارات واللغة وإمكانية الوصول.',
    editProfile: 'تعديل الملف الشخصي',
    changePassword: 'تغيير كلمة المرور',
    notificationPrefs: 'تفضيلات الإشعارات',
    themeLayout: 'المظهر والتخطيط',
    roleManagement: 'إدارة الأدوار',
    roleManagementText: 'أنشئ وعدّل الأدوار المستخدمة في لوحة التحكم.',
    addRole: 'إضافة دور جديد',
    roleNameEn: 'اسم الدور (إنجليزي)',
    roleNameAr: 'اسم الدور (عربي)',
    saveRole: 'حفظ الدور',
    noRoles: 'لا توجد أدوار مخصصة حتى الآن.',
    role: 'الدور',
    roleAssigned: 'الدور المعين',
    selectRole: 'اختر دورًا',
  }
}

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: null as string | null,
    refreshToken: null as string | null,
    user: null as UserProfile | null,
    isAuthenticated: false,
    locale: (localStorage.getItem('hrms_locale') as 'en' | 'ar') || 'en',
    theme: (localStorage.getItem('hrms_theme') as 'light' | 'dark') || 'light',
    roles: [
      { id: 'superadmin', name: { en: 'Super Admin', ar: 'المشرف العام' } },
      { id: 'manager', name: { en: 'Manager', ar: 'مدير' } },
      { id: 'hr', name: { en: 'HR', ar: 'الموارد البشرية' } },
      { id: 'employee', name: { en: 'Employee', ar: 'موظف' } }
    ] as RoleDefinition[],
  }),
  getters: {
    currentRole: (state) => state.user?.role || 'employee',
    roleLabel: (state) => {
      const role = state.roles.find((role) => role.id === state.user?.role)
      return role ? role.name[state.locale] : state.user?.role || 'Employee'
    },
    isSuperAdmin: (state) => state.user?.role === 'superadmin',
    isManager: (state) => state.user?.role === 'manager',
    isHR: (state) => state.user?.role === 'hr',
    isEmployee: (state) => state.user?.role === 'employee',
  },
  actions: {
    setTokens(access: string, refresh: string) {
      this.accessToken = access
      this.refreshToken = refresh
      this.isAuthenticated = true
      localStorage.setItem('hrms_access_token', access)
      localStorage.setItem('hrms_refresh_token', refresh)
    },
    setUser(user: UserProfile) {
      this.user = user
    },
    logout() {
      this.accessToken = null
      this.refreshToken = null
      this.user = null
      this.isAuthenticated = false
      localStorage.removeItem('hrms_access_token')
      localStorage.removeItem('hrms_refresh_token')
    },
    async login(email: string, password: string) {
      const response = await loginService({ email, password })
      const { access, refresh, user } = response.data
      this.setTokens(access, refresh)
      this.setUser(user as UserProfile)
      return response
    },
    initialize() {
      const access = localStorage.getItem('hrms_access_token')
      const refresh = localStorage.getItem('hrms_refresh_token')
      if (access && refresh) {
        this.accessToken = access
        this.refreshToken = refresh
        this.isAuthenticated = true
      }
      const savedLocale = localStorage.getItem('hrms_locale') as 'en' | 'ar' | null
      const savedTheme = localStorage.getItem('hrms_theme') as 'light' | 'dark' | null
      if (savedLocale) {
        this.locale = savedLocale
      }
      if (savedTheme) {
        this.theme = savedTheme
      }
      document.documentElement.classList.toggle('dark', this.theme === 'dark')
      document.documentElement.setAttribute('dir', this.locale === 'ar' ? 'rtl' : 'ltr')
    },
    async loadProfile() {
      const response = await fetchProfile()
      this.setUser(response.data as UserProfile)
    },
    setLocale(locale: 'en' | 'ar') {
      this.locale = locale
      localStorage.setItem('hrms_locale', locale)
      document.documentElement.setAttribute('dir', locale === 'ar' ? 'rtl' : 'ltr')
    },
    toggleTheme() {
      this.theme = this.theme === 'dark' ? 'light' : 'dark'
      localStorage.setItem('hrms_theme', this.theme)
      document.documentElement.classList.toggle('dark', this.theme === 'dark')
    },
    addRole(nameEn: string, nameAr: string) {
      const newRole: RoleDefinition = {
        id: `${nameEn.toLowerCase().replace(/\s+/g, '-')}-${Date.now()}`,
        name: { en: nameEn, ar: nameAr }
      }
      this.roles.push(newRole)
    },
    t(key: keyof typeof translations.en) {
      return translations[this.locale][key] || translations.en[key] || key
    }
  },
})
