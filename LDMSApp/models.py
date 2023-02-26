from django.db import models
from django.utils import timezone
#
#The model for keeping track of all the financial 
#transaction of the patient
class FinancialSummmaryRecord(models.Model):
	verbose_name 	= 'Financial Summary'
	#the payable due by the patient
	paid_amount 	= models.CharField(max_length=50)
	#total amount payable that a patient is supposed to make 
	#to the facility
	total_fee_due 	= models.CharField(max_length=50)
	balance 		= models.CharField(max_length=50)
	total_test 		= models.CharField('Total #test', max_length=50, default=1)
	total_cost 		= models.CharField(max_length=50)
	total_discount 	= models.CharField(max_length=50)
	def __str__(self):
		return self.paid_amount
#
#
#
#
#model for requesting for test to be done
#This should be use by the clinician or any person deem fit 
#to request for a test 
#
class PatientInfo(models.Model):
	verbose_name = 'PatientInfo'

	SEX = [
		('M', 'male'),
		('F', 'Female'),
		('O', 'Other')
	]

	financial_summary 	= models.ForeignKey(FinancialSummmaryRecord, on_delete=models.CASCADE)
	patient_name 		= models.CharField(max_length=100)
	date_of_birth 		= models.DateField('DOB')
	age 				= models.IntegerField()
	sex 				= models.CharField(max_length=1, choices=SEX)
	diagnosis 			= models.CharField(max_length=300)
	facility 			= models.CharField('clinic/dept', max_length=500)
	patient_id 			= models.CharField(max_length=1000)
	requester 			= models.CharField(max_length=200)
	insuarance_type 	= models.CharField(max_length=200)
	insuarance_number 	= models.CharField(max_length=200)
	mobile_number 		= models.IntegerField()
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

#registeration of facilities
#this is the model to register a laboratory facility so that clinicians can have access to
#it should define the various test capacities of the laboratory
class LaboratoryRegisteration(models.Model):

	laboratory_name 	= models.CharField(max_length=200)
	address 			= models.TextField()
	Tel 				= models.IntegerField()
	digital_address 	= models.CharField(max_length=100)
	region_of_location 	= models.CharField(max_length=2, choices=REGIONS)
	services_rendering 	= models.CharField(max_length=500)

	def __str__(self):
		return self.laboratory_name



#this is the model for hospitals to sign up to our system
#so that they can make request through it
class HospitalREgisteration(models.Model):

	hospital_name 		= models.CharField(max_length=200)
	name_of_laboratory 	= models.CharField(max_length=200)
	address 			= models.TextField()
	Tel 				= models.IntegerField()
	digital_address 	= models.CharField(max_length=100)
	region_of_location 	= models.CharField(max_length=2, choices=REGIONS)

	def __str__(self):
		return self.hospital_name


class TestResults(models.Model):
	pass
