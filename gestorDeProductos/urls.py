from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('registrar/', views.registrar),
    path('index/', views.index),
    path('mantenedor/', views.mantenedor),
    path('galeria/',views.galeria),
    path('login/',views.login)
]