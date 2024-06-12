from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from login.forms import UserLoginForm


def loginUser(request):
    # redirect to the index page if the user is already logged in
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == "POST":
        # Get the username and password from the request's POST data
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate the user with the provided username and password
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If the user is authenticated, log them in and redirect to the last page they were on
            login(request, user)
            return redirect(request.GET.get('next', 'index'))
        else:
            # If the authentication fails, display an error message
            messages.error(request, "Username or password is incorrect")
            return redirect("login")

    return render(request, "login/login.html")


def logoutUser(request):
    logout(request)
    return redirect("/")


def registerUser(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("confirm_password")

        # Check if the passwords match
        if password == password2:
            # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken")
                return redirect("register")
            # Check if the email is already taken
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already taken")
                return redirect("register")
            else:
                # Create a new user
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()
                # Log in the user after account creation
                login(request, user)
                messages.success(request, "User created and logged in")
                return redirect("index")
        else:
            messages.error(request, "Passwords do not match")
            return redirect("register")

    context = {}
    return render(request, "login/register.html", context)
