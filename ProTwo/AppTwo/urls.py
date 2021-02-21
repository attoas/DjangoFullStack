from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from AppTwo import views

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url (r'^$',views.index,name='index'),
    path('users',views.users,name='users')

]
