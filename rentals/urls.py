from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/book/', views.book_product, name='book_product'),
]
