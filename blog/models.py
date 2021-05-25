from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Tweet(models.Model):
    class Meta(object):
        db_table = 'tweet'

    name = models.CharField(
        'name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body = models.CharField(
        'body', blank=False, null=False, max_length=140, db_index=True, default=""
    )
    image = CloudinaryField(
        'image', blank=True, null=True
    )
    #like_count = models.PositiveIntegerField(
    #   default= 0, null=True
    #)
    created_at = models.DateTimeField(
        'created_datetime', blank=True, auto_now_add=True
    )
    # updated_at = models.DateTimeField(
    #    'Updated Datetime', blank=True, auto_now=True
    #)

