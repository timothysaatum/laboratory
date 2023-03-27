from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from .managers import CustomManager
from django.conf import settings
User = settings.AUTH_USER_MODEL



class Facility(AbstractBaseUser):
	email = models.EmailField(unique=True)
	facility_name = models.CharField(max_length=200)
	city_or_town = models.CharField(max_length=200)
	region_of_location = models.CharField(max_length=300)
	address = models.CharField(max_length=100)
	digital_address = models.CharField(max_length=100)
	is_a_delivery = models.BooleanField(default=False)
	telephone = models.CharField(max_length=20)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	date_joined = models.DateTimeField(default=timezone.now)
	is_a_laboratory = models.BooleanField(default=False) 

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = 	['telephone']

	objects = CustomManager()
	class Meta:
		verbose_name_plural = 'facilities'


	def __str__(self):
		return self.facility_name
	
	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		return True


	@property
	def is_staff(self):
		return self.is_admin

class Profile(models.Model):
	email = models.EmailField()
	telephone = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	facility_name = models.ForeignKey(Facility, on_delete=models.SET_NULL, null=True, blank=True)
	city_or_town = models.CharField(max_length=200)
	region_of_location = models.CharField(max_length=200)
	digital_address = models.CharField(max_length=100)
	
	def __str__(self):
		return f'{self.user.facility_name} Profile'


			

