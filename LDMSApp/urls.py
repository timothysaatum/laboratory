from django.urls import path
from . import views

urlpatterns = [
	path('', views.DefaultView.as_view(), name='default'),
	path('home', views.home_page, name='home'),
	path('laboratory/add/', views.add_laboratory, name='lab'),
	path('hospital/add/', views.add_hospital, name='hospital'),
	path('delivery/add/', views.delivery, name='delivery'),
]