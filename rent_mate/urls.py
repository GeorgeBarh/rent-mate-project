from django.contrib import admin
from django.urls import path, include
from home import views as home_views
    from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('products/', include('products.urls')),
    path('rentals/', include('rentals.urls')),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
     
