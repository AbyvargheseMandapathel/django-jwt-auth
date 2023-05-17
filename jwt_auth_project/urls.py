# jwt_auth_project/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('jwt_auth_app.urls')),  # Include your app's URLs
]
