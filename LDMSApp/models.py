from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
#


User = get_user_model()
SEX = [
	('M', 'male'),
	('F', 'Female'),
	('O', 'Other')
]

#The model for keeping track of all the financial 
#transaction of the patient
class FinancialSummmaryRecord(models.Model):
	#the payable due by the patient
	#payee = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
	amount_paid 	= models.CharField(max_length=50)
	#total amount payable that a patient is supposed to make 
	#to the facility
	total_fee_due 	= models.CharField(max_length=50)
	balance 		= models.CharField(max_length=50)
	total_test 		= models.CharField('Total #test', max_length=50, default=1)
	total_cost 		= models.CharField(max_length=50)
	total_discount 	= models.CharField(max_length=50)
	def __str__(self):
		return self.amount_paid
#
#
#
#
#model for requesting for test to be done
#This should be use by the clinician or any person deem fit 
#to request for a test 
#
class Patient(models.Model):

	hospital 	= models.ForeignKey('Hospital', on_delete=models.SET_NULL, blank=True, null=True)
	laboratory = models.ForeignKey('Laboratory', on_delete=models.SET_NULL, blank=True, null=True)
	delivery = models.ForeignKey('Delivery', on_delete=models.SET_NULL, blank=True, null=True)
	patient_name 		= models.CharField(max_length=100)
	date_of_birth 		= models.DateField('DOB')
	age 				= models.IntegerField()
	sex 				= models.CharField(max_length=1, choices=SEX)
	diagnosis 			= models.CharField(max_length=300)
	department 			= models.CharField('clinic/dept', max_length=500)
	patient_id 			= models.CharField(max_length=1000)
	#requester 			= models.CharField(max_length=200)
	mobile_number 		= models.CharField(max_length=15)
	#to keep track of the time the record entered
	time_issued 		= models.DateField(timezone.now())

	def __str__(self):
		return self.patient_name

REGIONS = [
		('UW', 'Upper West'),
		('VR', 'Volta'),
		('NR', 'Northen'),
		('AS', 'Ashanti'),
		('GR', 'Greater Accra'),
		('OR', 'Oti Region'),
		('SR', 'Savannah'),
		('UE', 'Upper East')
	]
#
#registeration of laboraotry facilities
#this is the model to register a laboratory facility so that clinicians can have access to
#it should define the various test capacities of the laboratory
class Laboratory(models.Model):
	laboratory_manager = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
	email = models.EmailField(unique=True)
	laboratory_name 	= models.CharField(max_length=200)
	address 			= models.CharField(max_length=200)
	Tel 				= models.CharField(max_length=20)
	digital_address 	= models.CharField(max_length=100)
	region_of_location 	= models.CharField(max_length=50)
	#let them list the the tests they do in laboratory separated by commas or spaces
	#this is to enable it to be displayed using strip method
	services_rendering 	= models.CharField(max_length=500)

	class Meta:
		verbose_name_plural = 'Laboratories'

	def __str__(self):
		return self.laboratory_name
#
#
#
#this is the model for hospitals to sign up to our system
#so that they can make request through it
class Hospital(models.Model):
	hospital_head = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
	email = models.EmailField(unique=True)
	hospital_name 		= models.CharField(max_length=200)
	#name_of_laboratory 	= models.CharField(max_length=200)
	address 			= models.CharField(max_length=200)
	Tel 				= models.CharField(max_length=15)
	digital_address 	= models.CharField(max_length=100)
	region_of_location 	= models.CharField(max_length=2, choices=REGIONS)

	def __str__(self):
		return self.hospital_name
#
#
#
#
#this is to be use to submit the results of a test to 
#the hospital requesting the test
#
class Result(models.Model):
	#patient = models.OneToOneField(Patient, on_delete=models.SET_NULL, blank=True, null=True)
	sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, blank=True, null=True)
	specimen_id = models.CharField(max_length=100)
	upload_pdf = models.FileField(upload_to='static/test_results', null=True, blank=True)
	sample_appearance_when_received = models.CharField(max_length=400)
	sample_container = models.CharField(max_length=100)
	parameter = models.TextField(null=True, blank=True)
	value = models.TextField(null=True, blank=True)
	comments = models.TextField()
	send_to = models.ForeignKey(Hospital, on_delete=models.SET_NULL, blank=True, null=True)
	send_by = models.CharField(max_length=30)

	def __str__(self):
		return self.sender
#
#
#
#
#model for requesting for a test
class Test(models.Model):
	TEST_STATUS = [
		('T', 'Timed'),
		('F', 'Fasting'),
		('S', 'STAT')
	]
	date = models.CharField(max_length=20)
	referring_facility = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	#facility = models.CharField(max_length=200)
	refer_sample_to = models.ForeignKey(Laboratory, on_delete=models.SET_NULL, blank=True, null=True)
	age_of_patient = models.CharField(max_length=150)
	gender = models.CharField(max_length=2, choices=SEX)
	type_of_test = models.CharField(max_length=200)
	sample_no = models.CharField(max_length=500)
	sample_type = models.CharField(max_length=200)
	test_status = models.CharField(max_length=2, choices=TEST_STATUS)
	department = models.CharField(max_length=100)
	brief_notes = models.TextField()
	name_of_referring_clinician = models.CharField(max_length=100)
	add_delivery = models.ForeignKey('Delivery', on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return self.sample_no

class Delivery(models.Model):
	company_name = models.CharField(max_length=100)
	owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	location = models.CharField(max_length=100)
	digital_address = models.CharField(max_length=20)
	address = models.CharField(max_length=100)
	tel = models.CharField(max_length=15)

	class Meta:
		verbose_name_plural = 'Deliveries'
	def __str__(self):
		return self.owner.username