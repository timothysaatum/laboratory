from django.contrib import admin
from .import models


class FinancialSummmaryRecordAdmin(admin.ModelAdmin):
	list_display = [
		'payee', 'amount_paid', 'total_fee_due', 'balance', 'total_test',
		'total_cost', 'total_discount'	
	]

class PatientAdmin(admin.ModelAdmin):
	list_display = [
		'patient_name', 'age', 'sex', 'diagnosis', 'facility', 'patient_id', 'mobile_number', 
		'insuarance_type', 'insuarance_number'
	]

class LaboratoryAdmin(admin.ModelAdmin):
	list_display = [
		'laboratory_name', 'address', 'Tel', 'digital_address', 'region_of_location'
	]

class HospitalAdmin(admin.ModelAdmin):
	list_display = ['hospital_name', 'region_of_location', 'address', 'Tel', 'digital_address']

class TestResultAdmin(admin.ModelAdmin):
	list_display = [#
		'laboratory', 'patient', 'specimen_id', 'upload_pdf', 'parameter', 'value',
		'comments', 'send_to'
	]

class RequestTestAdmin(admin.ModelAdmin):
	list_display = [
		'facility', 'request_to', 'specimen_id', 
		'department', 'description', 'name_requestor'
	]

admin.site.register(models.Laboratory, LaboratoryAdmin)
admin.site.register(models.Patient, PatientAdmin)
admin.site.register(models.FinancialSummmaryRecord, FinancialSummmaryRecordAdmin)
admin.site.register(models.Hospital, HospitalAdmin)
admin.site.register(models.TestResult, TestResultAdmin)
admin.site.register(models.RequestTest, RequestTestAdmin)