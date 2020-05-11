from django.db import models

# Create your models here.
class Community(models.Model):
    username = models.CharField(max_length=30)
    # upload = models.FileField(upload_to='uploads/')
    image = models.ImageField(upload_to='timeline_photo/%Y/%m/%d')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)