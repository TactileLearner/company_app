# my_company_app/admin_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from common_app.models import CustomUser, Employee, Client, Project, Task, LeaveRequest # Import your custom user model
from django.db.models import Q 
from django.utils import timezone
# # Helper function to check if a user is a superuser or staff
# def is_admin_or_staff(user):
#     return user.is_superuser or user.is_staff

def is_admin(user):
    return hasattr(user, 'user_role') and user.user_role == 'Admin'

@login_required
@user_passes_test(is_admin, login_url='/unauthorized/') # Redirects to /unauthorized/ if not admin
def admin_dashboard_view(request):
    # I. Overview & Metrics
    total_users = CustomUser.objects.count()
    total_employees = Employee.objects.count()
    total_clients = Client.objects.count()
    total_projects = Project.objects.filter(Q(status='Active') | Q(status='Pending')).count() # Example: count active/pending projects
    pending_leave_requests = LeaveRequest.objects.filter(status='Pending').count()
    overdue_tasks = Task.objects.filter(due_date__lt=timezone.now(), status__in=['Pending', 'In Progress']).count()

    # II. Quick Actions & Management Links (URLs will be added in admin_app/urls.py if they are custom views)
    # For now, these will mostly point to Django admin or placeholders.

    # III. Recent Activity
    recent_users = CustomUser.objects.order_by('-date_joined')[:5] # Get last 5 registered users
    recent_projects = Project.objects.order_by('-start_date')[:5] # Get last 5 added projects
    latest_leave_requests = LeaveRequest.objects.order_by('-requested_at')[:5] # Assuming 'requested_at' field
    # You might need to add a 'last_updated' or 'modified_at' field to your Task model
    # For now, let's just order by due_date for tasks, or creation date if available
    recent_tasks = Task.objects.order_by('-due_date')[:5] # Or order by created_at if you add it

    context = {
        'total_users': total_users,
        'total_employees': total_employees,
        'total_clients': total_clients,
        'total_projects': total_projects,
        'pending_leave_requests': pending_leave_requests,
        'overdue_tasks': overdue_tasks,
        'recent_users': recent_users,
        'recent_projects': recent_projects,
        'latest_leave_requests': latest_leave_requests,
        'recent_tasks': recent_tasks,
    }
    return render(request, 'admin_app/dashboard.html', context)

@login_required
@user_passes_test(is_admin)
def user_list_view(request): # <--- This function must be present and correctly named
    """
    Displays a list of all custom users in the system.
    """
    users = CustomUser.objects.all().order_by('username')
    return render(request, 'admin_app/user_list.html', {'users': users, 'message': 'Manage All Users'})