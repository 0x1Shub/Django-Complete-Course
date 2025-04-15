from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length = 255)
    age = models.PositiveIntegerField()
    grade = models.CharField(max_length = 5)

    def __str__(self):
        return self.name