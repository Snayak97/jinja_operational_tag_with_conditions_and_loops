from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':3500,'b':500,'c':60}
    return render(request,'condition.html',context=d)



def loops(request):
    d={'name':'SOUMYA'}
    return render(request,'loops.html',d)
