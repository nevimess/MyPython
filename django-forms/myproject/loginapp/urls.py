from django.conf.urls import url
from . import views


app_name = 'loginapp'
urlpatterns = [
    url(r'^',views.showlogin, name='showlogin'),
    url(r'^getname',views.getname, name='getname')
]