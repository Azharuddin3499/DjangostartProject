from django.shortcuts import render
from services.models import Services


# Create your views here.
def services(request):
    serviceData =Services.objects.all()
    return render(request,"services.html",{'serviceData':serviceData})
