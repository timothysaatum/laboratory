from django import forms
from .models import Hospital, Result, Test, Patient, Delivery
from django.utils.translation import gettext_lazy as _


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
class AddLaboratory(forms.Form):
	laboratory_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your laboratory name'}))
	address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your address of location'}))
	Tel = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your phone'}))
	digital_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your digital address'}))
	region_of_location = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'placeholder':'Enter your region of location'}), choices=REGIONS)
	services_rendering = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter your test you run'}))



class AddHospital(forms.ModelForm):
	class Meta:
		model = Hospital
		fields = '__all__'

class AddDelivery(forms.ModelForm):
	class Meta:
		model = Delivery
		fields = '__all__'

class ResultsForm(forms.ModelForm):
	class Meta:
		model = Result
		exclude = ('laboratory', )
		#fields = '__all__'

class AddPatientForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = '__all__'

class TestForm(forms.ModelForm):
	class Meta:
		model = Test
		exclude = ('date', 'referring_facility')


		