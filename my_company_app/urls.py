# D:\my_company_app\my_company_app\urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from common_app.views import home_view, login_view # Ensure both are imported here

urlpatterns = [
    path('admin/', admin.site.urls), # Django Admin site
    path('', home_view, name='home'), # Root URL mapped to common_app's home view

    # Include common_app's URLs under '/common/' prefix with its namespace
    path('common/', include('common_app.urls', namespace='common_app')),

    # Include other app URLs under their respective prefixes with their namespaces
    path('employee/', include('employee_app.urls', namespace='employee_app')),
    path('hr/', include('hr_app.urls', namespace='hr_app')),
    path('manager/', include('manager_app.urls', namespace='manager_app')),

    # Assuming you have client_app and admin_app, include them with their namespaces
    # It's crucial that the prefix (e.g., 'admin_app/') matches your app's intended URL prefix,
    # and the namespace (e.g., 'admin_app') matches app_name in that app's urls.py.
    path('client/', include('client_app.urls', namespace='client_app')),
    path('admin_app/', include('admin_app.urls', namespace='admin_app')), # Use 'admin_app/' for consistency
]

# This block is for serving media and static files in development
# It should remain as it is, outside the main urlpatterns definition,
# as it's conditional on settings.DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)