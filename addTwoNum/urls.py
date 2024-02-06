from django.urls import path
from addTwoNum import views

urlpatterns = [
    path('twonum/',views.addTwo),
    path('evenodd/',views.evenodd),

]
