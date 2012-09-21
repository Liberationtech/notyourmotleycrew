from notyourmotleycrew.timelinejs.models import Timeline
from notyourmotleycrew.timelinejs.models import Event

from django.contrib import admin

class TimelineAdmin(admin.ModelAdmin):
    list_display = ('headline', 'startdate')
    list_filter = ('status',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('startdate', 'headline',)
    list_filter = ('timeline',)

admin.site.register(Timeline, TimelineAdmin)
admin.site.register(Event, EventAdmin)

