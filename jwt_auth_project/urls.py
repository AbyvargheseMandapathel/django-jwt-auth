# jwt_auth_project/urls.py

from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('jwt_auth_app.urls')),  # Include your app's URLs
    path('', TemplateView.as_view(template_name='index.html')),
    path('login/', TemplateView.as_view(template_name='index.html')),
    path('home/', TemplateView.as_view(template_name='index.html')),
]
urlpatterns += staticfiles_urlpatterns()
