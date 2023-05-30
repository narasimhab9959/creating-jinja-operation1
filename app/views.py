from django.shortcuts import render

# Create your views here.

def wish(request):
    d={'a':40,'b':99}
    return render(request,'wish.html',context=d)