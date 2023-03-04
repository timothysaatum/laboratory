from django.forms import ModelForm
from .models import Laboratory

class LabSignUp(ModelForm):
	class Meta:
		model = Laboratory
		fields = '__all__'