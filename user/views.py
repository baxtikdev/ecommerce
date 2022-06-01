from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from .models import CustomUser as User, Code

from user.forms import LoginForm
# from .forms import CodeForm
from .utils import send_sms


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user and user.user.is_verify:
                login(request,user)
                return redirect('index')
    return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            phone = request.POST['phone']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
        except:
            return redirect('register')
        if password2 == password1:
            User.objects.create_user(username=username,phone_number=phone,password=password1)
            user = authenticate(request,username=username,password=password1)
            if user:
                try:
                    code = Code.objects.get(user=user)
                    code.save()
                except:
                    code = Code.objects.create(user=user)

                send_sms(code.number, user.phone_number)
                request.session['pk'] = user.pk
                return render(request,'auth/verify_sms.html')
    return render(request, 'auth/register.html',{})

def verify(request):
    pk = request.session.get('pk')
    if pk:
        user = User.objects.get(id=pk)
        code = Code.objects.get(user_id=pk)
        if not request.POST:
        #!1234567A@baxtiyor
            num = request.POST['number']
            if str(code.number) == num:
                login(request, user)
                return redirect('index')
            else:
                return redirect('log_in')
    return render(request, 'auth/verify_sms.html')

def log_out(request):
    logout(request)
    return redirect('log_in')
