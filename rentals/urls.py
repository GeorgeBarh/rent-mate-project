from django.urls import path
from . import views
from .webhooks import stripe_webhook  


urlpatterns = [
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('book/<int:pk>/', views.book_product, name='book_product'),
    path('create-checkout-session/<int:booking_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-cancel/', views.payment_cancel, name='payment_cancel'),
    path('stripe/webhook/', stripe_webhook, name='stripe_webhook'), 
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
 
]


