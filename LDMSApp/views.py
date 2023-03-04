from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import LabSignUp

#home view
class HomeView(TemplateView):
	template_name = 'LDMSApp/index.html'


#paid sign up
class SingUpView(TemplateView):
	template_name = 'LDMSApp/sign-up.html'

def laboratory_sign_up(request):
	if request.method == 'POST':
		l_form = LabSignUp(request.Post)
	l_form = LabSignUp()
	return render(request, 'LDMSApp/lab-sign-up.html', {'l_form':l_form})