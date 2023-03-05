from django.urls import path
from . import views

urlpatterns = [
	path('sign-up', views.sign_up, name='signup'),
	#path('hospital', views.hospital_sign_up, name='hospital'),
	#path('delivery', views.delivery_sign_up, name='delivery')
]
