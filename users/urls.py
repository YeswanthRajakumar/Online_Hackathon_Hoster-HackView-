from urllib import request

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin-register/', views.AdminUserRegisteration, name='admin-user-registration'),
    path('innovator-register/', views.InnovatorUserRegisteration, name='innovator-user-registration'),
    path('login/', views.loginPage, name='user-login'),
    path('logout/', views.logoutuser, name='user-logout'),
]
