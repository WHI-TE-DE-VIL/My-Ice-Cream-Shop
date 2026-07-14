from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Home.models import Contact


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signin(request):
    # 1. Catch already logged-in users and bounce them to the profile page
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        username_input = request.POST.get('username')
        password_input = request.POST.get('password')

        user = authenticate(request, username=username_input, password=password_input)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Invalid username or password. Please try again!")

    return render(request, 'sign_in.html')


def signup(request):
    # 2. Catch already logged-in users here as well
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username_input = request.POST.get('username')
        email_input = request.POST.get('email')
        password_input = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password_input != confirm_password:
            messages.error(request, "Passwords do not match. Please verify!")
            return render(request, 'sign_up.html')

        if User.objects.filter(username=username_input).exists():
            messages.error(request, "This username is already taken. Try another!")
            return render(request, 'sign_up.html')

        if User.objects.filter(email=email_input).exists():
            messages.error(request, "An account with this email already exists.")
            return render(request, 'sign_up.html')

        # Creates an administrative Superuser automatically
        user = User.objects.create_superuser(
            username=username_input,
            email=email_input,
            password=password_input,
            first_name=first_name,
            last_name=last_name
        )
        user.save()

        login(request, user)
        return redirect('profile')

    return render(request, 'sign_up.html')


def menu(request):
    return render(request, 'menu.html')


def findstore(request):
    return render(request, 'find_store.html')


def ourstory(request):
    return render(request, 'ourstory.html')


def locations(request):
    return render(request, 'locations.html')


def scoop(request):
    return render(request, 'scoop_detail.html')


def flavours(request):
    return render(request, 'flavours.html')


@login_required(login_url='sign_in')
def my_profile(request):
    return render(request, 'profile.html')


# ✨ Forcefully terminates active user sessions immediately upon request
def logout_view(request):
    logout(request)
    return redirect('sign_in')


def contactus(request):
    if request.method == "POST":
        namev = request.POST.get("name")
        emailv = request.POST.get("email")
        subjectv = request.POST.get("subject")
        messagev = request.POST.get("message")

        contact = Contact(name=namev, email=emailv, subject=subjectv, message=messagev)
        contact.save()

        messages.success(request, f"Thank you, {namev}! Your message was recorded.")
        return redirect('home_page')

    return render(request, 'contactus.html')
