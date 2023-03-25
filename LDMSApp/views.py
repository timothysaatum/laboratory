from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
#from django.http import JsonResponse
#from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
from .forms import (AddLaboratory, AddHospital, ResultsForm, AddPatientForm, TestForm, AddDelivery)
#from django.contrib.auth.models import User
#from django.utils import timezone
from django.contrib.auth import get_user_model
import datetime
from . models import (Laboratory, Test, Hospital, Result, Delivery)
#from channels.layers import get_channel_layer
#from asgiref.sync import async_to_sync
from django.conf import settings
from users.models import CustomUser

#class HomeView(TemplateView):
#	template_name = 'LDMSApp/index.html'
#
#	def get_context(self, **kwargs):
#		context = super().get_context_data(**kwargs)
#		context['req_form'] = RequestTestForm()
#		context['add_form'] = AddTestResultsForm()
#
#		return context
#
#	def form_valid(self, form):
#		pass

User = get_user_model()


@login_required
def home_page(request):
	if request.method == 'POST':
		req_form = TestForm(request.POST)
		add_form = ResultsForm(request.POST, request.FILES)
		#print(req_form)

		#checking to see if the submitted form is valid
		if req_form.is_valid():
			#taking logged in user first name and last name
			#requester = User.objects.get(username=request.user.username)
			#requester = request.user
			hospital = request.user.facility #Hospital.objects.get(hospital_head=request.user).hospital_name
			#facility = hospital.hospital_name
			#getting the other user parameters from the form when a user submits a test request form
			request_to = req_form.cleaned_data['refer_sample_to']
			type_of_test = req_form.cleaned_data['type_of_test']
			specimen_id = req_form.cleaned_data['sample_no']
			speciment_type = req_form.cleaned_data['sample_type']
			test_status = req_form.cleaned_data['test_status']
			department = req_form.cleaned_data['department']
			description = req_form.cleaned_data['brief_notes']
			name_requestor = req_form.cleaned_data['name_of_referring_clinician']
			#date = req_form.cleaned_data['date']
			age_of_patient = req_form.cleaned_data['age_of_patient']
			date = datetime.datetime.now()
			gender = req_form.cleaned_data['gender']
			#creating send test results form
			#patient = TestResult.objects.filter(patient=patient).value()
			#adding test request to the data base
			Test.objects.create(date=date, referring_facility=hospital, refer_sample_to=request_to, 
				age_of_patient=age_of_patient, gender=gender, type_of_test=type_of_test, 
				sample_no=specimen_id, sample_type=speciment_type, test_status=test_status, 
				department=department, brief_notes=description, name_of_referring_clinician=name_requestor)

		elif add_form.is_valid():
			send_from = Laboratory.objects.get(laboratory_manager=request.user)
			patient = add_form.cleaned_data['patient']
			specimen_id = add_form.cleaned_data['specimen_id']
			upload_pdf = add_form.cleaned_data['upload_pdf']
			sample_appearance_when_received = add_form.cleaned_data['sample_appearance_when_received']
			sample_container = add_form.cleaned_data['sample_container']
			parameter = add_form.cleaned_data['parameter']
			value = add_form.cleaned_data['value']
			comments = add_form.cleaned_data['comments']
			send_to = add_form.cleaned_data['send_to']
			send_by = add_form.cleaned_data['send_by']
			Result.objects.create(laboratory=send_from, patient=patient, specimen_id=specimen_id, upload_pdf=upload_pdf,
				sample_appearance_when_received=sample_appearance_when_received, sample_container=sample_container,
				parameter=parameter, value=value, comments=comments, send_to=send_to, send_by=send_by)
			#redirecting users to the homepage
			return HttpResponseRedirect(reverse('home'))
	#redisplaying an invalid form to the user
	req_form = TestForm()

	add_form = ResultsForm()
	#get all deliveries and display with their appropriate distances so that
	#the user can select which one they want
	deliveries = Delivery.objects.all()
	#display the test requested by the user
	all_test_requested = Test.objects.filter(referring_facility=request.user)
	#display the results requested by the user
	results = Result.objects.filter(sender=request.user)
	#print(deliveries, all_test_requested, results)
	return render(request, 'LDMSApp/index.html', {'req_form':req_form, 'add_form':add_form, 'all_test_requested':all_test_requested, 'deliveries':deliveries, 'results':results})
#
#
#view for adding a laboratory to the database
@login_required
def add_laboratory(request):
	if request.method == 'POST':
		lab_form = AddLaboratory(request.POST)
		if lab_form.is_valid():
			laboratory_manager = User.objects.get(id=request.user.id)
			address = lab_form.cleaned_data['address']
			Tel = lab_form.cleaned_data['Tel']
			digital_address = lab_form.cleaned_data['digital_address']
			regions = lab_form.cleaned_data['region_of_location']
			region_of_location = ', '.join(regions[:len(regions) - 1]) + ' and ' + str(regions[-1])
			services_rendering = lab_form.cleaned_data['services_rendering']
			laboratory_name=lab_form.cleaned_data['laboratory_name']
			#create a laboratory in the data base
			laboratory = Laboratory.objects.create(
					laboratory_manager=laboratory_manager, 
					laboratory_name=laboratory_name, address=address, Tel=Tel, 
					digital_address=digital_address, region_of_location=region_of_location, 
					services_rendering=services_rendering)
			return redirect('home')
	lab_form = AddLaboratory()

	return render(request, 'LDMSApp/lab.html', {'lab_form':lab_form})

@login_required
def add_hospital(request):
	if request.method == 'POST':
		form = AddHospital(request.POST)
		if form.is_valid():
			h_name = form.cleaned_data['hospital_name']
			form.save()
			return redirect('home')
	form = AddHospital()

	return render(request, 'LDMSApp/hospital.html', {'form':form})
#
@login_required
def delivery(request):
	if request.method == 'POST':
		form = AddDelivery(request.POST)
		if form.is_valid():
			form.cleaned_data['company_name']
			form.save()
			return redirect('home')
	form = AddDelivery()

	return render(request, 'LDMSApp/delivery.html', {'form':form})