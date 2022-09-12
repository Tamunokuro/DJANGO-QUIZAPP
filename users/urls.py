from re import template
from django.urls import path
from . import views
from .forms import AccountLoginForm
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

app_name = 'account'

urlpatterns = [
    path('', TemplateView.as_view(template_name='users/base.html'), name='home'),
    path('register/', views.register, name='register'),
    path('login/',  auth_views.LoginView.as_view(template_name='users/login.html', next_page = '/',
         form_class=AccountLoginForm), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout')

]