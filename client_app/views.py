from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def client_dashboard_view(request):
    return render(request, 'client_app/dashboard.html', {'message': 'Welcome to the Client Dashboard!'})
