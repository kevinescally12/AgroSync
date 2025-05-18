# accounts/urls.py
from django.urls import path
from . import views
from accounts.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='home'),

    # Dashboards
    path('dashboard/agricultor/', views.dashboard_agricultor, name='dashboard_agricultor'),
    path('dashboard/ingeniero/', views.dashboard_ingeniero, name='dashboard_ingeniero'),
    path('dashboard/cooperativa/', views.dashboard_cooperativa, name='dashboard_cooperativa'),
    
]
