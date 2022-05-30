from tkinter import CASCADE
from django.contrib.auth.models import User
from django.db import models
from hostel.models import hostel, hostel_block, room, allocate_room


# Create your models here.
class student_report_problem(models.Model):
    student = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    problem_type = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.ImageField(blank=True, null=True, upload_to="images/" )
    hostel = models.ForeignKey(hostel, default='', on_delete=models.CASCADE)
    block_name = models.ForeignKey(hostel_block, default='', on_delete=models.CASCADE)
    room_name = models.ForeignKey(room, default='', on_delete=models.CASCADE)
    feedback = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.problem_type


class warden_report_problem(models.Model):
    warden = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    problem_title = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    hostel = models.ForeignKey(hostel, default='', on_delete=models.CASCADE)
    block_name = models.ForeignKey(hostel_block, default='', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.problem_title