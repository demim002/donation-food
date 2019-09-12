from django.shortcuts import render
#from django.http import HttpResponse
from .models import posting
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login

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
