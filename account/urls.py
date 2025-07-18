from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import SecureLogoutView


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', SecureLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile')
    #path('password-reset/', views.password_reset, name='password-reset'), @todo implement me
    #path('settings/', views.settings, name='settings') @todo implement me
]

