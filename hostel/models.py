from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class hostel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.name


class hostel_block(models.Model):
    block_name = models.CharField(max_length=20)
    hostel_name = models.ForeignKey(hostel, default='', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.block_name