from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreateBook.as_view()),
    path('get/', GetBook.as_view()),
    path('update/', UpdateBook.as_view()),
    path('delete/', DeleteBook.as_view())
]