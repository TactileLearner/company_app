# D:\my_company_app\common_app\urls.py

from django.urls import path
from . import views

app_name = 'common_app'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'), # This is the key line
    path('unauthorized/', views.unauthorized_view, name='unauthorized'),
    path('register/', views.register_view, name='register'),
    path('user-dashboard/', views.user_dashboard_view, name='user_dashboard'), # Active
    path('staff-dashboard/', views.staff_dashboard_view, name='staff_dashboard'), # Active
]