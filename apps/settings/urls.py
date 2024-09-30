from django.urls import path

from apps.settings.views import index, contact_views

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact_views, name='contact'),
]
