from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 255)
    age = models.IntegerField(max_length = 2)
    course = models.CharField()

    def __str__(self):
        return self.name
