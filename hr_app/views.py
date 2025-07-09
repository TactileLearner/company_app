# hr_app/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def is_hr(user):
    # This is where the error would occur if user_role isn't present
    return hasattr(user, 'user_role') and user.user_role == 'HR'

@login_required
@user_passes_test(is_hr, login_url='/unauthorized/') # <-- This is where the error from image_473238.png occurred for manager
def hr_dashboard_view(request):
    # ... logic for HR dashboard ...
    context = {
        'hr_specific_data': 'Some data for HR',
    }
    return render(request, 'hr_app/dashboard.html', context)