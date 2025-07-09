# D:\my_company_app\common_app\views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Employee, Client, CustomUser # Import your models (ensure CustomUser has 'user_role' field)

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages # Import messages


# --- Helper Function for User Access Checks ---
def is_admin_or_staff(user):
    """
    Checks if a user is a superuser or a staff member.
    Used for general staff dashboards or admin-like access.
    """
    return user.is_superuser or user.is_staff

# --- Core Authentication Views ---
def login_view(request):
    """
    Handles user login.
    """
    if request.user.is_authenticated:
        # If user is already logged in, redirect them based on their role
        return redirect('common_app:dashboard_redirect')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {user.username}!") # Optional success message
                # Redirect to 'next' URL if provided, otherwise to the dashboard_redirect
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('common_app:dashboard_redirect')
            else:
                messages.error(request, "Invalid username or password.") # Error message
                form.add_error(None, "Invalid username or password.") # Also add to form for display
    else:
        form = AuthenticationForm()
    return render(request, 'common_app/login.html', {'form': form})

@login_required # Ensures only logged-in users can attempt to logout
def logout_view(request):
    """
    Handles user logout.
    Ensures logout only happens via POST request for security.
    """
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You have been successfully logged out.") # Added success message
        return redirect('common_app:login') # Redirect to the login page after logout
    # If a GET request somehow reaches logout, just redirect them home or to login
    # This prevents direct URL access for logout (which is insecure)
    return redirect('common_app:home') # Or redirect to 'common_app:login'


# --- Main Landing Page ---
def home_view(request):
    """
    Renders the home/landing page. If user is authenticated, redirects to their specific dashboard.
    """
    if request.user.is_authenticated:
        return redirect('common_app:dashboard_redirect') # Redirect authenticated users to their specific dashboard
    return render(request, 'common_app/home.html')

# --- Centralized Dashboard Redirection Logic ---
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
            return redirect('admin_app:dashboard') # Changed from 'it-admin' to 'admin_app' as per your folder name
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
        # This will render common_app/staff_dashboard.html
        return render(request, 'common_app/staff_dashboard.html', {'user': user, 'message': 'Welcome Staff!'})
    else:
        # Default for any other authenticated user (e.g., standard users)
        # This will render common_app/user_dashboard.html
        return render(request, 'common_app/user_dashboard.html', {'user': user, 'message': 'Welcome User!'})

# --- Generic Dashboards for Direct Access (if needed, otherwise accessed via dashboard_redirect) ---
@login_required
def user_dashboard_view(request):
    """
    Generic dashboard for regular authenticated users (e.g., 'Employee' role if not in separate app).
    This view will be hit if dashboard_redirect falls through to it.
    """
    return render(request, 'common_app/user_dashboard.html', {'message': 'Welcome to your Dashboard!'})

@login_required
@user_passes_test(is_admin_or_staff, login_url='common_app:unauthorized')
def staff_dashboard_view(request):
    """
    Generic dashboard for staff members (not Superuser, Admin, or Manager explicitly).
    This view will be hit if dashboard_redirect falls through to it.
    """
    return render(request, 'common_app/staff_dashboard.html', {'message': 'Welcome to the Staff Dashboard!'})

# --- Unauthorized Access View ---
def unauthorized_view(request):
    """
    Displays a message for users who try to access a page they don't have permission for.
    """
    return render(request, 'common_app/unauthorized.html', {'message': 'You do not have permission to access this page.'})

# --- Registration View ---
def register_view(request):
    if request.method == 'POST':
        # You should ideally use a custom form for CustomUser if you have extra fields
        form = UserCreationForm(request.POST) # Consider using CustomUserCreationForm here
        if form.is_valid():
            user = form.save()
            # If you have a user_role field, you might want to set a default here for new registrations
            # e.g., user.user_role = 'Employee'
            # user.save()
            login(request, user) # Automatically log in the new user
            messages.success(request, "Registration successful! Welcome!") # Add success message
            return redirect('common_app:dashboard_redirect')
        else:
            messages.error(request, "Registration failed. Please correct the errors below.") # Add error message
    else:
        form = UserCreationForm() # Consider using CustomUserCreationForm here
    return render(request, 'common_app/register.html', {'form': form})