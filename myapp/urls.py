from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/create/', views.department_create, name='department_create'),
    path('departments/<int:id>/update/', views.department_update, name='department_update'),
    path('departments/<int:id>/delete/', views.department_delete, name='department_delete'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('employees/<int:id>/update/', views.employee_update, name='employee_update'),
    path('employees/<int:id>/delete/', views.employee_delete, name='employee_delete'),
]
