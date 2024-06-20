from django.db import models

class Student(models.Model):
    first = models.CharField(max_length=200, blank=True, null=True)
    last = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length= 20)
    location = models.CharField(max_length=200)
    hobby = models.CharField(max_length=200)
    course = models.CharField(max_length= 200, default= "computer science")


    def __str__(self):
        return self.first
