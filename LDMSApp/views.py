from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
from .forms import AddLaboratory, AddHospital


def home_page(request):
	if request.method == 'POST':
		re_form = AddHospital(request.POST)
		sub_form = AddLaboratory(request.POST)
		if re_form.is_valid() and sub_form.is_valid():
			re_form.save()
			sub_form.save()
			return redirect('home')
	re_form = AddHospital()
	sub_form = AddLaboratory()
	return render(request, 'LDMSApp/index.html', {'re_form':re_form, 'sub_form':sub_form})
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
#
@login_required
def submit_results(request):
	return render(request, 'LDMSApp/results.html')