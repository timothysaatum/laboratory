from django.urls import path
from . views import notify_me

urlpatterns = [
	path('notification', notify_me, name='notify')
]