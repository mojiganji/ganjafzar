from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request, 'index.html')
    
def programming(request):
    return render(request, 'programming.html')

def neural(request):
    return render(request, 'neural.html')


def data(request):
    return render(request, 'data.html')


def machine(request):
    return render(request, 'machine.html')
