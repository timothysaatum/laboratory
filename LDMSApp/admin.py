from django.contrib import admin
from .import models


class FinancialSummmaryRecordAdmin(admin.ModelAdmin):
	list_display = [
		'amount_paid', 'total_fee_due', 'balance', 'total_test',
		'total_cost', 'total_discount'	
	]

class PatientAdmin(admin.ModelAdmin):
	list_display = [
		'patient_name', 'age', 'sex', 'diagnosis', 'department', 'hospital', 'laboratory', 'delivery', 'patient_id', 'mobile_number'
	]

class LaboratoryAdmin(admin.ModelAdmin):
	list_display = [
		'laboratory_name', 'laboratory_manager', 'address', 'Tel', 'digital_address', 'region_of_location'
	]

class HospitalAdmin(admin.ModelAdmin):
	list_display = ['hospital_name', 'region_of_location', 'address', 'Tel', 'digital_address']

class ResultAdmin(admin.ModelAdmin):
	list_display = [#
		'laboratory', 'patient', 'specimen_id', 'upload_pdf', 'parameter', 'value',
		'comments', 'send_to'
	]

class TestAdmin(admin.ModelAdmin):
	list_display = [
		'referring_facility', 'refer_sample_to', 'sample_no', 'date', 'age_of_patient', 'gender',
		'department', 'brief_notes', 'name_of_referring_clinician'
	]

class DeliveryAdmin(admin.ModelAdmin):
	list_display = [
		'company_name', 'owner', 'location', 
		'digital_address', 'address', 'tel'
	]

admin.site.register(models.Laboratory, LaboratoryAdmin)
admin.site.register(models.Patient, PatientAdmin)
admin.site.register(models.FinancialSummmaryRecord, FinancialSummmaryRecordAdmin)
admin.site.register(models.Hospital, HospitalAdmin)
admin.site.register(models.Result, ResultAdmin)
admin.site.register(models.Test, TestAdmin)
admin.site.register(models.Delivery, DeliveryAdmin)