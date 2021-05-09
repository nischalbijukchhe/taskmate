from django.urls import path #import django path
from users_app import views # connect my urls in view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.register, name = 'register'),
 #mention which view i need to connect with since it is an application i need to connect with view for the functionality
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]

