from django.contrib import admin
from blackboard.models import (
    Blackboard, BlackboardMembership, LoggedEvent
)

@admin.register(Blackboard)
class BlackboardAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'name', 'created')

@admin.register(BlackboardMembership)
class BlackboardMembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'board', 'member_since', 'last_read', 'last_write')

@admin.register(LoggedEvent)
class LoggedEventAdmin(admin.ModelAdmin):
    pass