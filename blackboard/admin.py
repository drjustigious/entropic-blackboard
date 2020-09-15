from django.contrib import admin
from blackboard.models import (
    Blackboard, BlackboardMembership, LoggedEvent
)

@admin.register(Blackboard)
class BlackboardAdmin(admin.ModelAdmin):
    pass

@admin.register(BlackboardMembership)
class BlackboardMembershipAdmin(admin.ModelAdmin):
    pass

@admin.register(LoggedEvent)
class LoggedEventAdmin(admin.ModelAdmin):
    pass