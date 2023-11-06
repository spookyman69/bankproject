from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect

from bankapp.models import Application


# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['password']
        cpassword = request.POST['confirmpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is already taken")
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, password=cpassword)
                user.save()
                print("user created")
                messages.info(request, "Registration Succesful")
                return render(request, 'login.html')
                # messages.info (request, "succesfuly")
                # messages.info (request, "username taken")
        else:
            messages.info(request, "Password does not match")
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("Login Successful")
            return redirect("/")
        else:
            messages.info(request, 'Invalid Credentials.')
            print("Login Failed")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def application(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        mail = request.POST['mail']
        address = request.POST['address']
        district = request.POST['first']
        branch = request.POST['second']
        acc = request.POST['acc']
        app = Application.objects.create(name=name, dob=dob, age=age, gender=gender, phone=phone, mail=mail, address=address, district=district,branch=branch,acctype=acc)
        app.save()
        messages.info(request,"Application Placed")
        return render(request, "application.html")
    else:
        return render(request, "application.html")
