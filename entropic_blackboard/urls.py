from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

admin.autodiscover()

import blackboard.views


urlpatterns = [
    path("", blackboard.views.atrium, name="atrium"),
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
]
