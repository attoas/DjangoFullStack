from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.

def index(request):
    #return HttpResponse("<em>My Second App</em>")
    return render(request,'AppTwo/index.html')

def HelpPage(request):
    helpdict = {'help_insert':"Hello I am from AppTwo/HelpPage.html !"}
    #return render(request,'index.html',context=my_dict)
    return render(request,'AppTwo/HelpPage.html',context=helpdict)


def users(request):
    #return HttpResponse("Hello World!")
    #users_dict ={'users_info': "I come from AppTwo.views.users"}
    #return render(request,'AppTwo/users.html',context=users_dict)
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'AppTwo/users.html',context=user_dict)
