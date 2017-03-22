from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpRequest, HttpResponse
from .models import user
from .forms import loginform
from django.template import RequestContext
from django.shortcuts import redirect

# Create your views here.
def viewUsers(request):
    userlist = user.objects.all()
    return render_to_response('myapp/viewUser.html',{'userlist': userlist})

def index(request):
    return render_to_response('myapp/login.html')

def login(request):
    username = 'Not logged in'
    if request.method =='POST':
        form = loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
    else:

        form = loginform()

    return render(request,'myapp/loggedin.html', {'username': username}, RequestContext(request))