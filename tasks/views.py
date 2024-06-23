from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your views here.
def home(request):
    return render(request,'home.html')


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request,'./signup.html', {'form':form})
        #print('Enviando formulario')
    #     
    else:
    #     # print(request.POST)
    #     # print('obteniendo datos')
        if request.POST['password1'] == request.POST['password2']:
    #         #register user
            try:
                user= User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])                             
                user.save()
                login(request,user)
                return redirect('tasks')
            except IntegrityError:
                return render(request,'./signup.html', {
                    'form':form,
                    'error': 'Username already exists'
                })
        return render(request,'./signup.html', {
                    'form':form,
                    'error': 'Password do not match'
                })
    
    # return render(request, 'signup.html',{
    #     'form': UserCreationForm
    # })
def tasks(request):
    return render(request, 'tasks.html')