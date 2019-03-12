from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponse
from menu.scripts.TestScript import LaunchNetCapture, function, StopNetCapture

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
    return render(request, 'pppoe_conf.html')

def StaticView(request):
    return render(request, 'static_conf.html')