# my_company_app/manager_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from common_app.models import CustomUser, Employee, Project, Task # Import relevant models

# Helper function to check if a user is a manager (is_staff=True)
def is_manager(user):
    return user.is_staff and user.user_role == 'Manager' # Assuming 'Manager' is the specific role name

@login_required
@user_passes_test(is_manager, login_url='common_app:login') # Redirect if not a manager
def manager_dashboard_view(request):
    # You might fetch some summary data here later
    return render(request, 'manager_app/dashboard.html', {'message': 'Welcome to the Manager Dashboard!'})

@login_required
@user_passes_test(is_manager, login_url='common_app:login')
def employee_list_view(request):
    # Managers can see employees in their department or under them
    # For simplicity, let's list all employees for now.
    # Later, we can filter based on the manager's department or direct reports.
    employees = Employee.objects.all().order_by('full_name')
    return render(request, 'manager_app/employee_list.html', {'employees': employees, 'message': 'Manage Team Members'})

@login_required
@user_passes_test(is_manager, login_url='common_app:login')
def project_list_view(request):
    # Managers can see projects they are associated with or oversee
    projects = Project.objects.all().order_by('name') # Fetch all for now
    return render(request, 'manager_app/project_list.html', {'projects': projects, 'message': 'Active Projects'})

@login_required
@user_passes_test(is_manager, login_url='common_app:login')
def task_list_view(request):
    # Managers can see tasks within their projects or assigned to their employees
    tasks = Task.objects.all().order_by('due_date') # Fetch all for now
    return render(request, 'manager_app/task_list.html', {'tasks': tasks, 'message': 'Assigned Tasks'})

# --- Placeholder for future CRUD operations (Create, Update, Delete) ---
# Example: Add a view to create a new project (requires a form)
# @login_required
# @user_passes_test(is_manager, login_url='/unauthorized/')
# def project_create_view(request):
#     if request.method == 'POST':
#         form = ProjectForm(request.POST)
#         if form.is_valid():
#             project = form.save(commit=False)
#             project.manager = request.user.employee_profile # Assuming a link
#             project.save()
#             return redirect('manager_app:project_list')
#     else:
#         form = ProjectForm()
#     return render(request, 'manager_app/project_form.html', {'form': form})