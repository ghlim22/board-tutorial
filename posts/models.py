from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from users.models import Profile

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="own_posts")
    profile = models.ForeignKey(to=Profile, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    body = models.TextField()
    image = models.ImageField(upload_to="post/", default="default.jpeg")
    likes = models.ManyToManyField(to=User, related_name="liked_posts", blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)
