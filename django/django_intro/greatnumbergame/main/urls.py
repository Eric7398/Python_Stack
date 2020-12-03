from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
	path('rng', views.rng),
    path('del', views.delete)

]