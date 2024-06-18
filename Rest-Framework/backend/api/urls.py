from django.urls import path
from . import views

urlpatterns = [
    path('welcome',views.welcome,name='welcome'),
    path('get', views.getEmployee, name='getemployee'),
    path('add', views.addEmployee, name='addemployee'),
    path('put/', views.putEmployee, name='putemployee'),
    path('patch/', views.patchEmployee, name='patchemployee'),
    path('delete/', views.deleteEmployee, name='deleteemployee'),
]
