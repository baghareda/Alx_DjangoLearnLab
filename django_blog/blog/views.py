from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404

from .forms import RegistrationForm, UserUpdateForm
from .models import Profile

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # hashes password automatically
            # ensure profile exists
            Profile.objects.get_or_create(user=user)
            login(request, user)  # auto-login after register
            messages.success(request, "Account created successfully. Welcome!")
            return redirect("home")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegistrationForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def profile(request):
    # ensure profile exists
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        uform = UserUpdateForm(request.POST, instance=request.user)
        # simple profile update (bio only)
        if uform.is_valid():
            uform.save()
            profile.bio = request.POST.get("bio", profile.bio)
            profile.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
        else:
            messages.error(request, "Fix the errors below.")
    else:
        uform = UserUpdateForm(instance=request.user)

    return render(
        request,
        "blog/profile.html",
        {"uform": uform, "profile": profile},
    )


def home(request):
    return render(request, "blog/home.html")
