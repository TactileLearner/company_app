# D:\my_company_app\employee_app\urls.py

from django.urls import path
from . import views

app_name = 'employee_app' # Namespace for employee-specific URLs

urlpatterns = [
    path('dashboard/', views.employee_dashboard_view, name='dashboard'), # Employee's main dashboard
    # Later add more paths for personal info, leave requests, task overview, etc.
]