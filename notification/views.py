from django.shortcuts import render
from LDMSApp.models import Test

def notify_me(request):
	re = Test.objects.all()
	return render(request, 'notification/notify.html', {'re':re})
