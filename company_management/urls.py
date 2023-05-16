from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_company', views.add_company, name='add_company'),
    path('delete_company/<int:pk>', views.delete_company, name='delete_company'),
    path('edit_company/<int:pk>', views.edit_company, name='edit_company'),
    path('add_branch', views.add_branch, name='add_branch'),
    path('edit_branch/<int:pk>', views.edit_branch, name='edit_branch')
]