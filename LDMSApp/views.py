from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
#from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
from .forms import (AddLaboratory, AddHospital, ResultsForm, AddPatientForm, TestForm, AddDelivery)
#from django.contrib.auth.models import User
#from django.utils import timezone
from django.contrib.auth import get_user_model
from users.models import Facility
import datetime
from . models import (Laboratory, Test, Hospital, Result, Delivery)
#from channels.layers import get_channel_layer
#from asgiref.sync import async_to_sync
from django.conf import settings
#from users.models import CustomUser


user = get_user_model()

'''
the default that is shown to a user that is not register
or has logged out of the app
'''
class DefaultView(TemplateView):
	template_name = 'LDMSApp/default.html'


@login_required
def home_page(request):
	if request.method == 'POST':
		req_form = TestForm(request.POST)
		add_form = ResultsForm(request.POST, request.FILES)
		'''
		checking to see if the user is submitting test request
		'''
		if req_form.is_valid():
			'''
			get the current logged in user and set them as the facility name
			since it is them sending th results
			'''
			hospital = Facility.objects.get(facility_name = request.user)

			'''
			processing the other form data
			'''
			request_to = req_form.cleaned_data['refer_sample_to']
			type_of_test = req_form.cleaned_data['type_of_test']
			specimen_id = req_form.cleaned_data['sample_no']
			speciment_type = req_form.cleaned_data['sample_type']
			test_status = req_form.cleaned_data['test_status']
			department = req_form.cleaned_data['department']
			description = req_form.cleaned_data['brief_notes']
			name_requestor = req_form.cleaned_data['name_of_referring_clinician']
			age_of_patient = req_form.cleaned_data['age_of_patient']
			date = datetime.datetime.now()
			gender = req_form.cleaned_data['gender']
			'''
			creating a test instance using data from the form
			'''
			Test.objects.create(date=date, referring_facility=hospital, refer_sample_to=request_to, 
				age_of_patient=age_of_patient, gender=gender, type_of_test=type_of_test, 
				sample_no=specimen_id, sample_type=speciment_type, test_status=test_status, 
				department=department, brief_notes=description, name_of_referring_clinician=name_requestor)
		
		else:
			req_form = TestForm(request.POST)
		'''
		checking to see if the user is submitting a result
		'''
		if add_form.is_valid():
			send_from = request.user.facility_name
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
			'''
			redirecting the user to the homepage after submitting the form
			'''
			return HttpResponseRedirect(reverse('home'))
		else:
			add_form = ResultsForm(request.POST)
	'''
	display the form if a get request is sent
	'''
	req_form = TestForm()

	add_form = ResultsForm()
	'''
	getting all the deliveries objects, all test objects and results objects available.
	according the logged in user
	'''
	deliveries = Delivery.objects.all()
	all_test_requested = Test.objects.filter(referring_facility=request.user)
	results = Result.objects.filter(sender=request.user)
	return render(request, 'LDMSApp/index.html', {'req_form':req_form, 'add_form':add_form, 'all_test_requested':all_test_requested, 'deliveries':deliveries, 'results':results})
#
#
#view for adding a laboratory to the database
@login_required
def add_laboratory(request):
	if request.method == 'POST':
		lab_form = AddLaboratory(request.POST)
		if lab_form.is_valid():
			laboratory_manager = Facility.objects.get(facility_name=request.user)
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