from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

def getname(request):
    your_name = "not logged in"
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            your_name = NameForm.cleaned_data['your_name']
    else:
        form = NameForm()

    return render(request, 'loginapp/loggedin.html', {'your_name': your_name})

def showlogin(request):
    return render(request, 'loginapp/login.html')
