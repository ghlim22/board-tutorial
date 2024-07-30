from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                related_name="profile")  # Using corresponding user's primary key as primary key.
    nickname = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    subjects = models.CharField(max_length=20)
    image = models.ImageField(upload_to="profile/", default="default.jpeg")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
