import datetime, pytz

from blackboard.models import LoggedEvent
from django.conf import settings


class BlackboardLogger:
    """
    A container class for functions that log user activity
    events to the database.
    """

    @classmethod
    def debug(message, user=None):
        log(message, user, LoggedEvent.LogSeverityLevel.DEBUG)

    @classmethod
    def info(message, user=None):
        log(message, user, LoggedEvent.LogSeverityLevel.INFO)

    @classmethod
    def warning(message, user=None):
        log(message, user, LoggedEvent.LogSeverityLevel.WARNING)

    @classmethod
    def error(message, user=None):
        log(message, user, LoggedEvent.LogSeverityLevel.ERROR)

    @classmethod
    def log(message, user, severity):
        log_event = LoggedEvent()
        log_event.message = message
        log_event.user = user
        log_event.severity = severity
        log_event.save()

        remove_old_log_entries(settings.DAYS_TO_KEEP_LOGGED_EVENTS)

    @classmethods
    def remove_old_log_entries(days_to_keep):
        """
        Remove all logged events that are older than
        'days_to_keep' days from the database.
        """
        now_utc = datetime.datetime.utcnow()
        delete_before_date = now_utc - datetime.timedelta(days=days_to_keep)

        events_to_delete = LoggedEvent.objects.filter(
            time__lt=delete_before_date
        )

        num_events_to_delete = len(events_to_delete)
        events_to_delete.delete()
        print("Deleted {} old logged events.".format(num_events_to_delete))