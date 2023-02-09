from django.urls import path
from . import views

urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('get-account', views.SingUpView.as_view(), name='sign-up')
]