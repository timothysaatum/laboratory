from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import AddLaboratory, AddHospital

#home view
class HomeView(TemplateView):
	template_name = 'LDMSApp/index.html'


def add_laboratory(request):
	if request.method == 'POST':
		form = AddLaboratory(request.POST)
		if form.is_valid():
			form.cleaned_data['laboratory_name']
			form.save()
			return redirect('results')
	form = AddLaboratory()

	return render(request, 'LDMSApp/lab.html', {'form':form})


def add_hospital(request):
	if request.method == 'POST':
		form = AddHospital(request.POST)
		if form.is_valid():
			form.cleaned_data['laboratory_name']
			form.save()
			return redirect('home')
	form = AddHospital()

	return render(request, 'LDMSApp/hospital.html', {'form':form})

def submit_results(request):
	return render(request, 'LDMSApp/results.html')