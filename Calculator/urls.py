from django.urls import path
from Calculator import views

urlpatterns = [
    path('calculator/',views.calculator)
]
