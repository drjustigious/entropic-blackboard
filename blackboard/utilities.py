import datetime, pytz

from blackboard.models import LoggedEvent
from django.conf import settings


class BlackboardLogger:
    """
    A container class for functions that log user activity
    events to the database.
    """

    @staticmethod
    def debug(message, user=None):
        BlackboardLogger.log(message, user, LoggedEvent.LogSeverityLevel.DEBUG)

    @staticmethod
    def info(message, user=None):
        BlackboardLogger.log(message, user, LoggedEvent.LogSeverityLevel.INFO)

    @staticmethod
    def warning(message, user=None):
        BlackboardLogger.log(message, user, LoggedEvent.LogSeverityLevel.WARNING)

    @staticmethod
    def error(message, user=None):
        BlackboardLogger.log(message, user, LoggedEvent.LogSeverityLevel.ERROR)

    @staticmethod
    def log(message, user, severity):
        log_event = LoggedEvent()
        log_event.message = message
        log_event.user = user
        log_event.severity = severity
        log_event.save()

        print(log_event)

        BlackboardLogger.remove_old_log_entries(settings.NUM_LOGGED_EVENTS_TO_KEEP)

    @staticmethod
    def remove_old_log_entries(num_events_to_keep):
        """
        Remove old logged events so that at most
        'num_events_to_keep' remain in the database.
        """
        events_to_keep = LoggedEvent.objects.all().order_by('-time')[:num_events_to_keep]
        events_to_delete = LoggedEvent.objects.all().exclude(pk__in=events_to_keep)

        events_to_delete.delete()