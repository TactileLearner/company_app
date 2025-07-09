# my_company_app/manager_app/urls.py

from django.urls import path
from . import views

app_name = 'manager_app'

urlpatterns = [
    path('dashboard/', views.manager_dashboard_view, name='dashboard'),
    path('employees/', views.employee_list_view, name='employee_list'), # New URL
    path('projects/', views.project_list_view, name='project_list'),   # New URL
    path('tasks/', views.task_list_view, name='task_list'),           # New URL
    # path('projects/new/', views.project_create_view, name='project_create'), # For later
]