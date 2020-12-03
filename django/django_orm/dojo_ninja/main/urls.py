from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
    path('dojo', views.dojo),
    path('delete', views.delete),

]