from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUp(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your preferred username'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g Your first name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your last name'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'e.g example@gmail.com'}))
	digital_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g XL-0876-0472'}))
	region_of_location = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g Upper West'}))
	class Meta:
		model = User
		fields = ['username','first_name', 'last_name', 'email', 'digital_address', 'region_of_location', 'password1', 'password2']


#class HospitalSignUp(UserCreationForm):
#	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your preferred username'}))
#	hospital_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g Advanz Hospital'}))
#	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g Administrator\'s first name'}))
#	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g Administrator\'s last name'}))
#	email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'e.g example@gmail.com'}))
#	digital_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g XL-0876-0472'}))
#	region_of_location = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g Upper West'}))
#	class Meta:
#		model = User
#		fields = ['username','first_name', 'last_name', 'hospital_name', 'email', 'digital_address', 'region_of_location', 'password1', 'password2']
#
#
#class DeliverySingUP(UserCreationForm):
#	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your preferred username'}))
#	company_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g Advanz Delivery'}))
#	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g Your first name'}))
#	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g Your last name'}))
#	email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'e.g example@gmail.com'}))
#	digital_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g XL-0876-0472'}))
#	region_of_location = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g Upper West'}))
#	class Meta:
#		model = User
#		fields = ['username','first_name', 'last_name', 'company_name', 'email', 'digital_address', 'region_of_location', 'password1', 'password2']