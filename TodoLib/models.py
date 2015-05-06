from django.db import models

# Create your models here.

class Todo(models.Model):
	name = models.CharField(max_length=16)
	description = models.CharField(max_length=160)
	deadline = models.DateField()
	progress = models.CharField(max_length=100)