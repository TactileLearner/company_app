from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def employee_dashboard_view(request):
    return render(request, 'employee_app/dashboard.html', {'message': 'Welcome to the Employee Dashboard!'})