from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length = 100),
    content = models.TextField()
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
