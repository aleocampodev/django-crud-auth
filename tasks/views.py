from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,'home.html')


def signup(request):
    if request.method == 'GET':
        #print('Enviando formulario')
        return render(request, 'singup.html',{
            'form': UserCreationForm
        })
    else:
        # print(request.POST)
        # print('obteniendo datos')
        if request.POST['password1'] == request.POST['password1']:
            #register user
            try:
                user= User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])                             
                user.save()
                return HttpResponse('User created successfully')
            except:
                return HttpResponse('username already exists')
        return HttpResponse('Password do not match')
    
    # return render(request, 'signup.html',{
    #     'form': UserCreationForm
    # })
