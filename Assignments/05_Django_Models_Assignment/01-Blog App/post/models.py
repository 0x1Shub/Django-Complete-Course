from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 1000)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
