from django.shortcuts import render, redirect
#from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
from .forms import (AddLaboratory, AddHospital, AddTestResultsForm, AddPatient, RequestTestForm, AddDelivery)
from django.contrib.auth.models import User
from . models import (Laboratory, RequestTest, Hospital, TestResult)


def home_page(request):
	if request.method == 'POST':
		req_form = RequestTestForm(request.POST)
		add_form = AddTestResultsForm(request.POST, request.FILES)
		#print(req_form)

		#checking to see if the submitted form is valid
		if req_form.is_valid() and add_form.is_valid():

			#taking logged in user first name and last name
			facility = request.user.first_name + request.user.last_name

			#getting the other user parameters from the form when a user submits a test request form
			request_to = req_form.cleaned_data['request_to']
			type_of_test = req_form.cleaned_data['type_of_test']
			specimen_id = req_form.cleaned_data['specimen_id']
			speciment_type = req_form.cleaned_data['speciment_type']
			test_status = req_form.cleaned_data['test_status']
			department = req_form.cleaned_data['department']
			description = req_form.cleaned_data['description']
			name_requestor = req_form.cleaned_data['name_requestor']
			date = req_form.cleaned_data['date']

			#creating send test results form
			patient = TestResult.objects.filter(patient=patient).value()


			#adding test request to the data base
			RequestTest.objects.create(facility=facility, request_to=request_to, type_of_test=type_of_test, 
				specimen_id=specimen_id, speciment_type=speciment_type, test_status=test_status, 
				department=department, description=description,	name_requestor=name_requestor, date=date)
			#redirecting users to the homepage
			return redirect('home')
		print(req_form.errors.as_data())
	req_form = RequestTestForm()
	add_form = AddTestResultsForm()
	all_test_requested = RequestTest.objects.all()
	return render(request, 'LDMSApp/index.html', {'req_form':req_form, 'all_test_requested':all_test_requested})
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