from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import SuscriberForm
# Create your views here.

def new_suscriber(request, template='subscribers/new_suscriber.html'):
    if request.method=='POST':
        form=SuscriberForm(request.POST)
        if form.is_valid():
             username=form.cleaned_data['username']
             password=form.cleaned_data['password']
             email=form.cleaned_data['email']
             user=User(username=username, email=email)
             user.set_password(password)
             user.save()
            
            return HttpResponseRedirect('/success/ ')
    else:
        form=SuscriberForm()
    return render(request, template, {'form':form})