from django.db import models

# Create your models here.

class Todo(models.Model):
	name = models.CharField(max_length=128)
	description = models.CharField(max_length=128)
	deadline = models.DateField()
	progress = models.DecimalField(max_digits=20, decimal_places=0)