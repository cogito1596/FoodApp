from django.shortcuts import render
from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout

# Create your views here.


def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            messages.success(
                request, f"Welcome {username}, Account has been  successfully created"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()

    return render(request, "users/registration.html", {"form": form})


def user_logout(request):
    logout(request)
    return render(request, "users/logout.html")


def profile(request):
    return render(request, "users/profile.html")
