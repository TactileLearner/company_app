# D:\my_company_app\common_app\admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Employee, Client, Project, Task, LeaveRequest

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        # Correctly add only 'user_role' to a new fieldset
        # Make sure 'user_role' is actually defined on your CustomUser model in models.py
        (('Role Information'), {'fields': ('user_role',)}),
    )
    # Ensure 'user_role' is present here, and NO other fields that don't exist on CustomUser.
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'user_role')
    search_fields = ('username', 'email', 'user_role')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'user_role')


# Register other models
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_id', 'department', 'job_title', 'manager', 'phone_number', 'address') # You can add phone_number, address here if they are on Employee model
    search_fields = ('user__username', 'employee_id', 'department', 'job_title')
    list_filter = ('department', 'job_title')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'contact_person', 'email', 'phone_number', 'address') # You can add phone_number, address here if they are on Client model
    search_fields = ('client_name', 'contact_person', 'email')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'client', 'manager', 'status', 'start_date', 'end_date')
    list_filter = ('status', 'client', 'manager')
    search_fields = ('project_name', 'description')
    raw_id_fields = ('client', 'manager')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'project', 'assigned_to', 'status', 'priority', 'due_date')
    list_filter = ('status', 'priority', 'project', 'assigned_to')
    search_fields = ('task_name', 'description')
    raw_id_fields = ('project', 'assigned_to')

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave_type', 'start_date', 'end_date', 'status', 'approved_by')
    list_filter = ('leave_type', 'status')
    search_fields = ('employee__user__username', 'reason')
    raw_id_fields = ('employee', 'approved_by')