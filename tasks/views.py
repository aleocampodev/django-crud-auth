from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    return HttpResponse('<h2>Hello world</h2>')


def helloworld(request):
    return render(request, 'signup.html',{
        'form': UserCreationForm
    })
