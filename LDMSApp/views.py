from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
from .forms import AddLaboratory, AddHospital, AddTestResults, AddPatient, MakeTestRequest, AddDelivery


def home_page(request):
	if request.method == 'POST':
		re_form = MakeTestRequest(request.POST)
		add_form = AddTestResults(request.POST)
		if re_form.is_valid() and add_form.is_valid():
			re_form.save()
			add_form.save()
			return redirect('home')
	re_form = MakeTestRequest()
	add_form = AddTestResults()
	return render(request, 'LDMSApp/index.html', {'re_form':re_form, 'sub_form':add_form})
#home view
#class HomeView(TemplateView):
#	template_name = 'LDMSApp/index.html'

	#@method_decorator(login_required)
	#def dispatch(self, *args, **kwargs):
	#	return super().dispatch(*args, **kwargs)

@login_required
def add_laboratory(request):
	if request.method == 'POST':
		form = AddLaboratory(request.POST)
		if form.is_valid():
			form.cleaned_data['laboratory_name']
			form.save()
			return redirect('results')
	form = AddLaboratory()

	return render(request, 'LDMSApp/lab.html', {'form':form})

@login_required
def add_hospital(request):
	if request.method == 'POST':
		form = AddHospital(request.POST)
		if form.is_valid():
			form.cleaned_data['laboratory_name']
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