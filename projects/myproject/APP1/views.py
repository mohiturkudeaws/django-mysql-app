from django.shortcuts import render
from .forms import DataForm
from . import models
from django.contrib import messages
#home page


def home(request):
    updates=models.Announcements.objects.all()
    admin=models.Administration.objects.all()
    return render(request,"home.html",{"updates":updates,"admin":admin})

#application
def application(request):
    if request.method=="POST":
     form=DataForm(request.POST or None,request.FILES)
     #incase form is validated
     if form.is_valid():
        form.save()
        messages.success(request,"you have successfully registered.")
        #clear the form
        form=DataForm()
        return render(request,"application.html",{'form':form})
     else:
        return render(request,"application.html",{'form':form})
    else:
        form=DataForm()
        return render(request,"application.html",{'form':form})




  

#login
def login(request):
    return render(request,"login.html")
