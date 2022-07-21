from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import get_user_model

User = get_user_model() # 이거 꼭 기억하기

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def login(request):
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login_fail.html')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signUp(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repeat']:
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], user_phone=request.POST['phone'], email=request.POST['email'], user_name=request.POST['name'])
            auth.login(request, new_user)
            return redirect('home')
    return render(request, 'sign_up.html')