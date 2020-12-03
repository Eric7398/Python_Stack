from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
		path('shows', views.main),
    path('shows/new', views.addpage),
    path('shows/create', views.addpageprocess),
    path('shows/<id>', views.showinfopage),
		path('shows/<id>/edit', views.editpage),
		path('shows/<id>/update', views.editpageprocess),
		path('shows/<id>/destroy', views.index),
]