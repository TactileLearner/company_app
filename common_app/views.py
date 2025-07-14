# D:\my_company_app\common_app\views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Employee, Client, CustomUser, Project, Task, LeaveRequest # Import all models needed
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone


# --- Helper Function for User Access Checks ---
def is_admin_or_staff(user):
    """Checks if a user is a superuser or a staff member."""
    return user.is_superuser or user.is_staff

# --- Core Authentication Views ---
def login_view(request):
    """Handles user login."""
    if request.user.is_authenticated:
        # Redirect to the dashboard_redirect view, which handles role-based redirection
        return redirect('common_app:dashboard_redirect')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {user.username}!")
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                # Redirect to the dashboard_redirect view after successful login
                return redirect('common_app:dashboard_redirect')
            else:
                messages.error(request, "Invalid username or password.")
                form.add_error(None, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'common_app/login.html', {'form': form})

@login_required
def logout_view(request):
    """Handles user logout. Ensures logout only happens via POST request for security."""
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You have been successfully logged out.")
        return redirect('common_app:login')
    return redirect('common_app:home')


# --- Main Landing Page ---
def home_view(request):
    """
    Renders the home/landing page.
    If user is authenticated, redirects to their specific dashboard.
    If not authenticated but a 'next' parameter exists, redirects to clean home page.
    """
    if request.user.is_authenticated:
        # If authenticated, always redirect to their dashboard via dashboard_redirect
        return redirect('common_app:dashboard_redirect')

    # If not authenticated, check if there's a 'next' parameter in the URL
    if 'next' in request.GET:
        # If a 'next' parameter exists and they are not authenticated,
        # redirect them to the clean home page URL to remove the parameter.
        return redirect('common_app:home')

    # If not authenticated and no 'next' parameter, render the home page
    return render(request, 'common_app/home.html')


# --- Centralized Dashboard Redirection Logic (BACK IN USE) ---
@login_required
def dashboard_redirect(request):
    """
    Redirects authenticated users to their specific dashboard based on their user_role.
    This is the primary post-login redirection point.
    """
    user = request.user

    # Prioritize redirection based on the 'user_role' field
    if hasattr(user, 'user_role'): # Safely check if user_role attribute exists on CustomUser
        if user.user_role == 'Admin':
            return redirect('admin_app:dashboard')
        elif user.user_role == 'Manager':
            return redirect('manager_app:dashboard')
        elif user.user_role == 'HR':
            return redirect('hr_app:dashboard')
        elif user.user_role == 'Employee':
            return redirect('employee_app:dashboard')
        elif user.user_role == 'Client':
            return redirect('client_app:dashboard')

    # Fallback logic if 'user_role' is not defined or doesn't match
    if user.is_superuser:
        return redirect('admin:index') # Direct superusers to Django's built-in admin
    elif user.is_staff:
        # For staff users without a specific 'Admin' or 'Manager' role assigned via user_role
        return render(request, 'common_app/staff_dashboard.html', {'user': user, 'message': 'Welcome Staff!'})
    else:
        # Default for any other authenticated user (e.g., standard users)
        return render(request, 'common_app/user_dashboard.html', {'user': user, 'message': 'Welcome User!'})

# --- Generic Dashboards (These are the actual views for user_dashboard.html and staff_dashboard.html) ---
@login_required
def user_dashboard_view(request):
    """Generic dashboard for regular authenticated users."""
    return render(request, 'common_app/user_dashboard.html', {'message': 'Welcome to your Dashboard!'})

@login_required
@user_passes_test(is_admin_or_staff, login_url='common_app:unauthorized')
def staff_dashboard_view(request):
    """Generic dashboard for staff members."""
    return render(request, 'common_app/staff_dashboard.html', {'message': 'Welcome to the Staff Dashboard!'})

# --- Unauthorized Access View ---
def unauthorized_view(request):
    """Displays a message for users who try to access a page they don't have permission for."""
    return render(request, 'common_app/unauthorized.html', {'message': 'You do not have permission to access this page.'})

# --- Registration View ---
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful! Welcome!")
            # Redirect to the dashboard_redirect view after successful registration
            return redirect('common_app:dashboard_redirect')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'common_app/register.html', {'form': form})