from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#class SignUp(forms.ModelForm):
#	model = UserCreationModel

class SignUp(UserCreationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your preferred username'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'e.g Your first name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your last name'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'e.g example@gmail.com'}))
	#password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Please Enter a strong Password'}))
	#password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Please Confirm Password'}))
	class Meta:
		model = User
		fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'e.g example@gmail.com'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ella'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Pure'}))
	class Meta:
		model = User
		fields = ['username','first_name', 'last_name', 'email']



class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['region_of_location', 'digital_address']
