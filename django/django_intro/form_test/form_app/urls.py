from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('users', views.create_user),
    path('create_user', views.create_user),

]