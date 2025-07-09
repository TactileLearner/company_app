# D:\my_company_app\common_app\urls.py

from django.urls import path
from . import views

app_name = 'common_app' # Defines the namespace for this app

urlpatterns = [
    path('', views.home_view, name='home'), # Base path for common_app (e.g., /common/)
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'), # General dashboard redirect
    path('unauthorized/', views.unauthorized_view, name='unauthorized'),
    path('register/', views.register_view, name='register'), # Added this line as per your comment
    path('user-dashboard/', views.user_dashboard_view, name='user_dashboard'), # For generic users
    path('staff-dashboard/', views.staff_dashboard_view, name='staff_dashboard'), # For general staff members
]