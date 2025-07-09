# D:\my_company_app\hr_app\urls.py

from django.urls import path
from . import views

app_name = 'hr_app' # Namespace for HR-specific URLs

urlpatterns = [
    path('dashboard/', views.hr_dashboard_view, name='dashboard'), # HR's main dashboard
    # Add other HR-specific paths here (e.g., employee management, payroll)
    # path('employees/', views.employee_management_view, name='employee_management'),
]