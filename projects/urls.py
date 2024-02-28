from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # Other URL patterns you might have commented out or included
]
