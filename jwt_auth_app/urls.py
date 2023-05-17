from django.urls import path
from .views import LoginView, LogoutView, HomeView
from django.views.generic import TemplateView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', HomeView.as_view(), name='home'),  # Uncomment this line
    # path('home/', HomeView.as_view(), {'template_name': 'index.html'}, name='home'),
    #path('home/', TemplateView.as_view(template_name='index.html')),
]
