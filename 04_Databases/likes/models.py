from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Likes(models.Model):
    likes = models.CharField(max_length=255)

class LikedItem(models.Model):
    # What user likes what objects
    like = models.ForeignKey(Likes, on_delete=models.CASCADE)

    # user: ForeignKey to User (django.contrib.auth.models)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()