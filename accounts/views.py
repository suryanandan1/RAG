from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .forms import SignupForm
from .models import UserProfile


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            employee_id = form.cleaned_data["employee_id"]
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]
            band = form.cleaned_data["band"]

            if User.objects.filter(username=employee_id).exists():
                form.add_error("employee_id", "Employee ID already exists.")
            else:
                user = User.objects.create_user(
                    username=employee_id,
                    password=password,
                    first_name=name
                )

                UserProfile.objects.create(
                    user=user,
                    band=band
                )

                login(request, user)
                return redirect("/chat/")
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect("/chat/")

    return render(request, "login.html", {"form": form})