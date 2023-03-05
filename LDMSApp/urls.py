from django.urls import path
from . import views

urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('add/laboratory/', views.add_laboratory, name='lab'),
	path('hospital/add', views.add_hospital, name='hospital'),
	path('submit/results', views.submit_results, name='results')
]