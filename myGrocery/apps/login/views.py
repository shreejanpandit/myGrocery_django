from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            print("invalid")
            return render(request, 'basics/login/index.html')
    else:
        return render(request, 'basics/login/index.html')


def logoutuser(request):
    auth.logout(request)
    return redirect('/login')


def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "email taken/ already registered")
                return render(request, 'basics/login/registration.html')

            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return render(request, 'basics/login/registration.html')

            else:
                user = User.objects.create_user(first_name=name, username=username, email=email, contact=contact,
                                                address=address, password=password1)
                user.save()
                print("User created")
                return render(request, 'basics/login/index.html')
        else:
            print("password not matched")
            return render(request, 'basics/login/registration.html')

            # return redirect('/')
    else:
        return render(request, 'basics/login/registration.html')
