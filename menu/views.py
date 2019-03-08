from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponse
from menu.scripts.TestScript import function

# Create your views here.

def IndexView(request):
    htmlvar = function()
    return render(request, 'index.html', {'htmlvar' : htmlvar})