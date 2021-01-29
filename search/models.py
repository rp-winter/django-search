from django.db import models

# Create your models here.

class Institute(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Users(models.Model):
    name = models.CharField(max_length=50)
    institution = models.ForeignKey(Institute, null=True, on_delete=models.SET_NULL)