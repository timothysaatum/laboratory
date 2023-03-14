from  . forms import AddPatientForm
from . models import Patient, RequestTest
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=RequestTest)
def create_patient(sender, instance, created, **kwargs):
	if created:
		Patient.objects.create(
            user=instance,
            email=instance.email,
            first_name=instance.first_name,
            last_name=instance.last_name)


@receiver(post_save, sender=RequestTest)
def save_patient(sender, instance, **kwargs):
    instance.patient.save()
