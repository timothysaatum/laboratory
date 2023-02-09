from django.shortcuts import render
from django.views.generic import TemplateView

#home view
class HomeView(TemplateView):
	template_name = 'LDMSApp/index.html'


#paid sign up
class SingUpView(TemplateView):
	template_name = 'LDMSApp/sign-up.html'