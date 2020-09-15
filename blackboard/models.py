from django.db import models
from django.contrib.auth.models import User


class LoggedEvent(models.Model):
    """
    An user activity event to be logged in the database.s
    """

    class LogSeverityLevel(models.IntegerChoices):
        DEBUG = 1
        INFO = 2
        WARNING = 3
        ERROR = 4

    time = models.DateTimeField(auto_now_add=True)
    severity = models.IntegerField(choices=LogSeverityLevel.choices)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    message = models.TextField()