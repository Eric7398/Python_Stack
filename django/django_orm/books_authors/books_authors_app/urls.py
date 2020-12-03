from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('author', views.authors),
    path('process', views.add_to_list),
    path('process_book/<id>', views.add_to_book_page),
    path('process_author/<id>', views.add_to_author_page),
    path('books/<id>', views.book_info),
    path('authors/<id>', views.author_info)
]