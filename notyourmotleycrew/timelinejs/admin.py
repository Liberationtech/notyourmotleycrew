from notyourmotleycrew.timelinejs.models import Timeline
from notyourmotleycrew.timelinejs.models import TimelineStartdate 
from notyourmotleycrew.timelinejs.models import EventStartdate
from notyourmotleycrew.timelinejs.models import Event

from django.contrib import admin

class TimelineStartdateInline(admin.StackedInline):
    model = TimelineStartdate
    max_num = 1

class EventStartdateInline(admin.StackedInline):
    model =  EventStartdate
    max_num = 1


class TimelineAdmin(admin.ModelAdmin):
    list_display = ('headline',)
    inlines = [
            TimelineStartdateInline,
            ]


class EventAdmin(admin.ModelAdmin):
    list_display = ('headline',)
    list_filter = ('timeline',)
    inlines = [EventStartdateInline,]

admin.site.register(Timeline, TimelineAdmin)
admin.site.register(Event, EventAdmin)

