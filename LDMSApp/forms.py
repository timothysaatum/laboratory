from django.forms import ModelForm
from .models import Laboratory, Hospital, TestResult, RequestTest, Patient, Delivery



class AddLaboratory(ModelForm):
	class Meta:
		model = Laboratory
		fields = '__all__'


class AddHospital(ModelForm):
	class Meta:
		model = Hospital
		fields = '__all__'

class AddDelivery(ModelForm):
	class Meta:
		model = Delivery
		fields = '__all__'

class AddTestResults(ModelForm):
	class Meta:
		model = TestResult
		fields = '__all__'

class AddPatient(ModelForm):
	class Meta:
		model = Patient
		fields = '__all__'

class MakeTestRequest(ModelForm):
	class Meta:
		model = RequestTest
		fields = '__all__'