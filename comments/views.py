from django.shortcuts import render
from comments.models import Comments
# Create your views here.
def comments(request):
    if request.method=='POST':
        name=request.POST['name']
        comment=request.POST['comm']
        data=Comments(name=name,comment=comment)
        data.save()
    return render(request,'comments.html')