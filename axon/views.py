from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




def login_view(request, user):
    login(request, user)
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'registration/logout.html')


# Create your views here.
@login_required(login_url='../login/')
def home_view(request):
    context = {
        "page_title": "Home",
        "body_title": "Welcome",
        "loggedInUser": request.user.username.upper(),
    }
    return render(request, "axon/home.html", context)
