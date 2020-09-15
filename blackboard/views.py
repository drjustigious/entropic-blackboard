from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from blackboard.models import LoggedEvent
from blackboard.utilities import BlackboardLogger


@login_required(login_url="login/")
def atrium(request):
    context = {
        "username": request.user.username if request.user else "N/A",
    }
    return render(request, "atrium.html", context)


@login_required(login_url="login/")
def logged_events(request):
    context = {
        "logged_events": LoggedEvent.objects.all().order_by('time')
    }
    BlackboardLogger.debug("Came to the logs page.", request.user)
    return render(request, "logged_events.html", context)