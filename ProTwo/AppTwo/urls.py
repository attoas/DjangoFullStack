from django.conf.urls import url
from django.urls import path
from AppTwo import views

urlpatterns = [
    url (r'^$',views.index,name='index'),
    path ('HelpPage',views.HelpPage,name='HelpPage')
    #path ('',views.index,name='index'),

]
