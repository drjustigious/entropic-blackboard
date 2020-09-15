import uuid

from django.db import models
from django.contrib.auth.models import User


class LoggedEvent(models.Model):
    """
    A user activity event to be logged in the database.
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

    def __str__(self):
        username = self.user.username if self.user else ""
        severity = self.get_severity_display().upper()
        time = self.time.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{time}] {severity} <{username}> {self.message}"


class Blackboard(models.Model):
    """
    A virtual blackboard that Django users can write stuff on.
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class BlackboardMembership(models.Model):
    """
    A model for tracking who is allowed to write on which table.
    Doesn't seem worth it to use Django Guardian for this.
    """
    board = models.ForeignKey(Blackboard, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    member_since = models.DateTimeField(auto_now_add=True)