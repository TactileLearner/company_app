# D:\my_company_app\admin_app\urls.py

from django.urls import path
from . import views

app_name = 'admin_app' # Namespace for admin-specific URLs

urlpatterns = [
    path('dashboard/', views.admin_dashboard_view, name='dashboard'), # Admin's main dashboard
    # Later add more paths for user management, role management, etc.
    path('users/', views.user_list_view, name='user_list'), # Example: Admin can list users
]