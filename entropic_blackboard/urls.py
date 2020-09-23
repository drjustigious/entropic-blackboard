from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

admin.autodiscover()

import blackboard.views


urlpatterns = [
    path("", blackboard.views.atrium, name="atrium"),
    path("blackboard/<uuid:board_uuid>/", blackboard.views.blackboard, name="blackboard"),
    path("logs/", blackboard.views.logged_events, name="logged_events"),

    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
]
