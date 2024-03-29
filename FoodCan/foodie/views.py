from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import posting
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

# Create your views here.

def homepage(request):
    return render(request = request,
                    template_name = "foodie/home.html",
                    context = {"postings": posting.objects.all()})

def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.info(request, f"account registered")
            login(request, user)
            return redirect("foodie:homepage")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "foodie/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request,
                 "foodie/register.html",
                 context= {"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out!")
    return redirect("foodie:homepage")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("foodie:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "foodie/login.html",
                    context={"form":form})
