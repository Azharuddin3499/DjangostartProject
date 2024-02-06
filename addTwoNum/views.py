from django.shortcuts import render

def addTwo(request):
    try:
        num1=int(request.POST['num1'])
        num2=int(request.POST['num2'])
        
        return render(request,'addtwo.html',{"result":num1+num2})
    except:
        return render(request,"addtwo.html")
    
def evenodd(request):
    try:
        rslt=''
        val1=int(request.POST['val'])
        if val1%2==0:
            rslt='Even'
        else:
            rslt='odd'
        return render(request,'evenodd.html',{"res":rslt})
    except:
        return render(request,"evenodd.html")
    