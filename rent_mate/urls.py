from django.contrib import admin
from django.urls import path, include
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('products/', include('products.urls')),
    path('rentals/', include('rentals.urls')),
]
