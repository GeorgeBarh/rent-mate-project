from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/book/', views.book_product, name='book_product'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('create-checkout-session/<int:booking_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-cancel/', views.payment_cancel, name='payment_cancel'),
]