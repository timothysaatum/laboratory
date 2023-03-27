from  . forms import AddPatientForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Hospital, Laboratory, Delivery
from django.contrib.auth import get_user_model
from users.models import Facility


@receiver(post_save, sender=Facility)
def create_patient(sender, instance, created, **kwargs):
    if created:
        if instance.is_a_laboratory == False and instance.is_a_delivery == False:
            print('is a hospital instance')
        elif instance.is_a_laboratory == False and instance.is_a_delivery != False:
            print('it was a delivery instance')

        else:
            print('it was a laboratory instance')
		
post_save.connect(create_patient, sender=Facility)