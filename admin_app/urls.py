# D:\my_company_app\admin_app\urls.py

from django.urls import path
from . import views

app_name = 'admin_app'

urlpatterns = [
    path('dashboard/', views.admin_dashboard_view, name='dashboard'), # Points to its own view
    path('users/', views.user_list_view, name='user_list'),
]