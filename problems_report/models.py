from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class student_report_problem(models.Model):
    student = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    problem_type = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    feedback = models.CharField(default='', null=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.problem_type


class warden_report_problem(models.Model):
    warden = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    problem_title = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.problem_title
