from django.db.models.signals import post_save
from django.contrib.auth.models import User # <- Sender
from django.dispatch import receiver # <- Receiver
from .models import Profile

# A receiver is a function that receives a signal and performs a task
# We also want to import a Profile from our models, because we want to create one

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()