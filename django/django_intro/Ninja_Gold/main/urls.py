from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
    path('new', views.index2),
    path('farm', views.farm),
    path('cave', views.cave),
    path('house', views.house),
    path('casino', views.casino),
    path('delete', views.delete),
]