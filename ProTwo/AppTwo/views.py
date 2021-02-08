from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<em>My Second App</em>")

def HelpPage(request):
    helpdict = {'help_insert':"Hello I am from AppTwo/HelpPage.html !"}
    #return render(request,'index.html',context=my_dict)
    return render(request,'AppTwo/HelpPage.html',context=helpdict)
