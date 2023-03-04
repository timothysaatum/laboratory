from django.contrib import admin
from .import models

class LaboratoryAdmin(admin.ModelAdmin):
	list_display = ['laboratory_name', 'region_of_location', 'address', 'Tel', 'digital_address']


admin.site.register(models.Laboratory, LaboratoryAdmin)