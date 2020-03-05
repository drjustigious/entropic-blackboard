from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Greeting

@login_required(login_url="login/")
def atrium(request):
    context = {
        "username": "Ruttomies"
    }

    return render(request, "atrium.html", context)