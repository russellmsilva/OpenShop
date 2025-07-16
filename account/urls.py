from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
    #path('register/', views.register, name='register'), @todo implement me
    #path('profile/', views.profile, name='profile'), @todo implement me
    #path('password-reset/', views.password_reset, name='password-reset'), @todo implement me
    #path('settings/', views.settings, name='settings') @todo implement me
]

