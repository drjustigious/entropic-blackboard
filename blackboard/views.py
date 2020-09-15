from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required(login_url="login/")
def atrium(request):
    context = {
        "username": request.user.username if request.user else "N/A",
    }

    return render(request, "atrium.html", context)