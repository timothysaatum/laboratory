from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.EmailField()
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	region_of_location = models.CharField(max_length=200)
	digital_address = models.CharField(max_length=100)
	
	def __str__(self):
		return f'{self.user.username} Profile'


			

