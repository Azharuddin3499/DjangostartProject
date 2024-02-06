from django.urls import path
from services import views

urlpatterns = [
    path('service/',views.services),
]
