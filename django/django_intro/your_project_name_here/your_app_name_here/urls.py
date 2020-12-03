from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),	   
    path('test', views.test),
    path('name/<aname>', views.hey),
    path('redirect', views.redirected_to_home),
]

#@app is in the string above ('/')
#def index():

#synced up with views.py in app name