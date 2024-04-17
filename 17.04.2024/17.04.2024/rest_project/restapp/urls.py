
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('users/', UserDisplayView.as_view(), name='user-list'),
    path('roles/', RoleCreateView.as_view(), name='role-create'),
    path('roleslist/', RoleDisplayView.as_view(), name='role-list'),
    path('userbyid/<int:pk>/', UserById.as_view(), name='userbyid'),
    path('login/', LoginView.as_view(), name='login'),


]
