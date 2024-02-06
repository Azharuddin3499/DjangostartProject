from django.shortcuts import render

def calculator(request):
    try:
        c=''
        num1=eval(request.POST['num1'])
        num2=eval(request.POST['num2'])
        opr=request.POST['opr']
        if opr=='+':
            c=num1+num2
        elif opr=='-':
            c=num1-num2
        elif opr=='*':
            c=num1*num2
        elif opr=='/':
            c=num1/num2
        else:
            c='Invalid Operator'    
        return render(request,'calculator.html',{'output':c})
    except:
        return render(request,'calculator.html')