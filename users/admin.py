from django.contrib import admin
from . models import Profile


class ProfileModelAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 
	'email', 'digital_address', 'region_of_location']

admin.site.register(Profile, ProfileModelAdmin)