from .models import Profile

from route.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save,sender = CustomUser)
def post_save_created_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)