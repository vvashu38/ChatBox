from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import chat
from django.http import JsonResponse
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/loggedin")
        else:
            messages.info(request, "invalid credential")
            return redirect("/")
    else:
        if request.user.is_authenticated:
            return redirect('loggedin')
        else:
            return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['rpassword']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                return redirect('/')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
    else:
        return render(request,'register.html')


def loggedin(request):
    if request.method == "POST":
        a = chat(dm=request.POST['msg'],un=request.user.username)
        a.save()
    else:
        list = chat.objects.all()
        return render(request,'chat.html',{'list': list})

def logout(request):
    auth.logout(request)
    return redirect('/')

def dms(request):
    list = chat.objects.all()
    return render('chat.html', {'list': list})