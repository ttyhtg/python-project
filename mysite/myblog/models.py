from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=191, primary_key=True)
    email = models.EmailField()
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    null_test = models.CharField(max_length=200, null=True)
    blank_test = models.CharField(max_length=200, null=True)