"""auth_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('register_hostel/', views.register_hostel, name='register_hostel'),
    path('hostel-list/', views.view_hostel, name='hostel-list'),
    path('update-hostel/<hostel_id>', views.update_hostel, name='update-hostel'),
    path('delete-hostel/<hostel_id>', views.delete_hostel, name='delete-hostel'),
    path('register_block/', views.register_hostel_block, name='register_block'),
    path('Blocks-list/', views.view_hostel_blocks, name='Blocks-list'),
    path('update-block/<hostel_block_id>', views.update_block, name='update-block'),
    path('delete-block/<hostel_block_id>', views.delete_block, name='delete-block'),
]
