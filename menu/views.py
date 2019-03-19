from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponse
from menu.scripts.TestScript import LaunchNetCapture, function, StopNetCapture
from . import forms
from . import models

# Create your views here.

def IndexView(request):
    #htmlvar = LaunchNetCapture()
    return render(request, 'index.html')    #, {'htmlvar' : htmlvar}

def StartCaptureView(request):
    process = LaunchNetCapture()
    return render(request, 'StartNetCapture.html', {'process' : process})

def StopCaptureView(request):
    process = StopNetCapture()
    return render(request, 'StopNetCapture.html', {'process' : process})

def PPPoEView(request):
    form = forms.pppoe_config_form
    if request.method == 'POST':
        form = forms.pppoe_config_form(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = forms.pppoe_config_form()
    return render(request, 'pppoe_conf.html', {'form' : form})

def StaticView(request):
    return render(request, 'static_conf.html')

def AddNewLinkView(request):
    form = forms.UrlAdditionForm
    if request.method == 'POST':
        form = forms.UrlAdditionForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = forms.UrlAdditionForm()
    return render(request, 'add_link.html', {'form':form})

def ListOfLinksView(request):
    urls = models.url.objects.all()
    return render(request, 'list_of_links.html', {'urls' : urls})