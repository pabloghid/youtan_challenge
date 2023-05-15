from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-company', views.add_company, name='add_company'),
    path('delete-company/<int:pk>', views.delete_company, name='delete_company'),
    path('edit-company/<int:pk>', views.edit_company, name='edit_company')
]