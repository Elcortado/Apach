from django.urls import path
from . import views

urlpatterns = [
    path('eventos/', views.events, name='eventos')
    
]