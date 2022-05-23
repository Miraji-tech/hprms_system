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
    path('register-room/', views.register_room, name='register-room'),
    path('rooms-registered/', views.view_rooms, name='rooms-registered'),
    path('update-room/<room_id>', views.update_room, name='update-room'),
    path('delete-room/<room_id>', views.delete_room, name='delete-room'),
    path('allocate-student-room/', views.allocate_room_student, name='allocate-student-room'),
    path('allocate-warden-block/', views.allocate_block_warden, name='allocate-warden-block'),
    path('student-allocations/', views.view_student_allocation, name='student-allocations'),
    path('warden-allocations/', views.view_warden_allocation, name='warden-allocations'),
    path('update-student-allocation/<allocate_room_id>', views.update_student_allocation_room, name='update-student-allocation'),
    path('delete-student-allocation/<allocate_room_id>', views.delete_student_allocation_room, name='delete-student-allocation'),
    path('update-warden-allocation/<allocate_block_id>', views.update_warden_allocation, name='update-warden-allocation'),
    path('delete-warden-allocation/<allocate_block_id>', views.delete_warden_allocation, name='delete-warden-allocation'),
]