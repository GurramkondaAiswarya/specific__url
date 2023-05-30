from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'aishu','age':3}
    return render(request,'wish.html',context=d)
