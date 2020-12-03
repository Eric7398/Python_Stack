from django.urls import path
from . import views

urlpatterns = [
	path('books', views.index),
	path('books/add', views.addbook),
	path('addproc', views.addproc),
	path('books/<id>', views.booksinfo),
	path('user/<id>', views.userinfo),
	path('addreview/<id>', views.addreview),
	path('del/<id>', views.deletereview),

	
	
	
]