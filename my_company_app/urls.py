# D:\my_company_app\my_company_app\urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from common_app.views import home_view, login_view # Ensure both are imported here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('common/', include('common_app.urls', namespace='common_app')), # Crucial for common_app URLs
    path('employee/', include('employee_app.urls', namespace='employee_app')),
    path('hr/', include('hr_app.urls', namespace='hr_app')),
    path('manager/', include('manager_app.urls', namespace='manager_app')),
    path('client/', include('client_app.urls', namespace='client_app')),
    path('admin_app/', include('admin_app.urls', namespace='admin_app')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)