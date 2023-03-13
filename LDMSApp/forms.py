from django import forms
from .models import Hospital, TestResult, RequestTest, Patient, Delivery
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

class AddTestResults(forms.ModelForm):
	class Meta:
		model = TestResult
		fields = '__all__'

class AddPatient(forms.ModelForm):
	class Meta:
		model = Patient
		fields = '__all__'

class RequestTestForm(forms.ModelForm):
	class Meta:
		model = RequestTest
		fields = ['request_to', 'type_of_test', 'specimen_id', 'speciment_type', 'test_status', 'department'
			, 'description', 'name_requestor', 'date'
		]
		
		widget = {
			'date':forms.DateInput(attrs={'placeholder':'MM/DD/YYYY'})
		}

		