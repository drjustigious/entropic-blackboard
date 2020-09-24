from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required

from blackboard.models import LoggedEvent, Blackboard
from blackboard.utilities import BlackboardLogger


@login_required()
@permission_required('blackboard.view_blackboard')
def atrium(request):
    """
    This is the view where a newly logged-in user will arrive.
    The view mainly lists the Blackboards available to that user.
    """

    available_blackboards = Blackboard.get_boards_available_to_user(request.user)
    print("Blackboards available to {}: {}".format(request.user.username, available_blackboards))

    context = {
        "user": request.user,
        "blackboards": available_blackboards
    }
    return render(request, "atrium.html", context)


@login_required()
@permission_required('blackboard.view_blackboard')
def blackboard(request, board_uuid):
    """
    This is the view of one particular blackboard.
    """
    blackboard = Blackboard.get_boards_available_to_user(request.user).filter(uuid=board_uuid).first()

    if not blackboard:
        BlackboardLogger.warning("Tried to access unavailable blackboard {}.".format(
            request.user.username if request.user else "(unknown user)",
            board_uuid
        ), request.user)

        raise Http404("The blackboard {} does not exist or the user '{}' does not have the permission to view it.".format(
            board_uuid,
            request.user.username if request.user else "unknown user"
        ))

    # Debuggg, add these to the model at some point:
    blackboard.width = 80
    blackboard.height = 24
    
    context = {
        "blackboard": blackboard,
        "user": request.user
    }
    return render(request, "blackboard.html", context)    


@login_required()
@permission_required('blackboard.view_loggedevent')
def logged_events(request):
    context = {
        "logged_events": LoggedEvent.objects.all().order_by('time')
    }
    BlackboardLogger.debug("Came to the logs page.", request.user)
    return render(request, "logged_events.html", context)