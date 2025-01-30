from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import os

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created:
    Token.objects.create(user=instance)

class PostList(models.Model):
  category = models.CharField(max_length= 50)
  title = models.TextField()
  subtitle = models.TextField()
  datePublished = models.DateTimeField(auto_now_add=True)
  dateUpdated = models.DateTimeField(auto_now=True)
  auth = models.CharField(max_length= 50)
  body = models.TextField()
  image = models.ImageField(upload_to='images/', null=True, blank=True)
  alt = models.CharField(max_length= 200)
  section = models.IntegerField(null=True, blank=True)
  order = models.IntegerField(null=True, blank=True)

  def delete(self, *args, **kwargs):
    # Delete the image file from the filesystem if it exists
    if self.image:
      try:
        os.remove(self.image.path)
      except Exception as e:
        print(f"Error deleting image {self.image.path}: {e}")
    super().delete(*args, **kwargs)

