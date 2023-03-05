from django.forms import ModelForm
from .models import Laboratory, Hospital



class AddLaboratory(ModelForm):
	class Meta:
		model = Laboratory
		fields = '__all__'


class AddHospital(ModelForm):
	class Meta:
		model = Hospital
		fields = '__all__'