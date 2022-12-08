from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= 'index'),
    path('nosotros/', views.about, name='nosotros'),
    path('eventos/', views.events, name='eventos'),
    path('actividad/', views.activity, name='actividad'),
    path('crear/', views.create, name='crear'),
    path('delete/', views.delete, name='delete'),

]