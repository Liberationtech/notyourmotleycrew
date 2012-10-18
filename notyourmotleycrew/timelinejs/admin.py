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
    #list_display = ('pk', 'url', 'headline', 'author', 'media_outlet' , 'facebook_total_count', 'added_by', 'startdate' )
    #list_display = ('pk', 'url', 'headline', 'author', 'media_outlet' , 'facebook_total_count', 'added_by' )
    list_display = ('pk', 'url', 'headline', 'author', 'media_outlet' , 'facebook_total_count', 'added_by', 'get_startdate' )
    list_filter = ('cleared_for_publication','timeline', 'added_by', 'media_outlet' )
    inlines = [EventStartdateInline,]


    def save_model(self, request, obj, form, change):
        """When creating a new object, set the creator field.
        """
        if not change:
            obj.added_by = request.user
        obj.save()

admin.site.register(Timeline, TimelineAdmin)
admin.site.register(Event, EventAdmin)

