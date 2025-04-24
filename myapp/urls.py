from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login),
    path('diagnostico/', views.Diagnostico),
    path('historial/', views.Historial)
]