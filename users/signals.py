from django.db.models.signals import post_save
from .models import Profile
from django.dispatch import receiver
from .forms import SignUp
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import Facility

user = get_user_model()

User = get_user_model()
@receiver(post_save, sender=Facility)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            email=instance.email,
            telephone=instance.telephone,
            address=instance.address)

@receiver(post_save, sender=Facility)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
