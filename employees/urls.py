from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home view
    path('add/', views.add_employee, name='add_employee'),  # Add employee
    path('update/<int:pk>/', views.update_employee, name='update_employee'),  # Update employee
    path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),  # Delete employee
    path('list/', views.employee_list, name='employee_list'),  # List for update/delete
    path('login/', auth_views.LoginView.as_view(template_name='employees/login.html'), name='login'),  # Correct path with quotes
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout view
]
