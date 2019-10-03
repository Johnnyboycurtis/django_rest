from django.db import models
from django.contrib.auth.models import User


class First(models.Model):
    form_choices = [('A', 'A'), ('B', 'B'),('C', 'C')]
    name = models.CharField(null=True, blank=True, max_length=100)
    form_type = models.CharField(null=True, blank=True, max_length=100, choices=form_choices)
    date_created = models.DateTimeField(auto_now_add=True)
    comments = models.CharField(null=True, blank=True, max_length=100)



class Second(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form_choices = [('A', 'A'), ('B', 'B'), ('C', 'C'),]
    name = models.CharField(null=True, blank=True, max_length=100)
    form_type = models.CharField(null=True, blank=True, max_length=100, choices=form_choices)
    date_created = models.DateTimeField(auto_now_add=True)
    comments = models.CharField(null=True, blank=True, max_length=100)

