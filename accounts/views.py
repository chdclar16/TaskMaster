from django.shortcuts import render, redirect
from accounts.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()

    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def logout_user(request):
    logout(request)
    return redirect("login")


def signup_user(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]

            if password == password_confirmation:
                user = User.objects.create_user(
                    username,
                    password=password,
                )
                login(request, user)
                return redirect("list_projects")
            else:
                form.add_error("password", "the passwords do not match")
    else:
        form = SignupForm()

    context = {
        "form": form,
    }
    return render(request, "registration/signup.html", context)
