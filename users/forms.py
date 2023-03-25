from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from .models import Facility


#form to display to the fron end for users to signup
REGIONS = [
		('Upper West', 'Upper West'),
		('Volta', 'Volta'),
		('Northen', 'Northen'),
		('Ashanti', 'Ashanti'),
		('Greater Accra', 'Greater Accra'),
		('Oti Region', 'Oti Region'),
		('Savannah', 'Savannah'),
		('Upper East', 'Upper East')
	]

class SignUp(UserCreationForm):
	email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'e.g example@gmail.com'}))
	facility_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your facility name'}))
	region_of_location = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'placeholder':'Check all that apply'}), choices=REGIONS)
	telephone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'+233 594 382 87'}))
	city_or_town = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Las Vegas'}))
	digital_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'XL-0476-0872'}))
	address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Tamale, NR'}))
	is_a_laboratory = forms.BooleanField()
	is_a_delivery = forms.BooleanField()
	#password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Please Enter a strong Password'}))
	#password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Please Confirm Password'}))
	class Meta:
		model = Facility
		fields = ['email', 'facility_name','is_a_laboratory', 'is_a_delivery', 'telephone', 'digital_address', 'address', 'city_or_town', 'region_of_location', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'e.g example@gmail.com'}))
	facility = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Ella'}))
	location = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Pure'}))
	class Meta:
		model = Facility
		fields = ['facility', 'location', 'telephone', 'email',]



class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['region_of_location', 'digital_address']
