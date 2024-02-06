from django.urls import path
from helloWorld import views

urlpatterns = [
    path('',views.helloworld),
    path('hello/',views.hello),

]
