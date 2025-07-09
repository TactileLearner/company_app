
from django.urls import path
from . import views

app_name = 'client_app'

urlpatterns = [
    path('dashboard/', views.client_dashboard_view, name='dashboard'),
    # Later add more paths for project status, communication, invoices, etc.
]