from django.urls import path
from . import views

urlpatterns = [
   path('', views.index), # views.index -> llama al metodo index dentro de views.py
]
