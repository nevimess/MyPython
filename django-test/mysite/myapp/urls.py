from django.conf.urls import url
from . import views


app_name = 'myapp'
urlpatterns = [
    url(r'^',views.index, name='index'),
    url(r'^login/',views.login, name='login'),
    url(r'loggedin/','myapp/loggedin.html', name='loggedin')
    #url(r'^getname',views.getname, name='getname')
]