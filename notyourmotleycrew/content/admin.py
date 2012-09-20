from notyourmotleycrew.content.models import NYMCImage
from notyourmotleycrew.content.models import Sign

from django.contrib import admin

class NYMCImageAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'caption')
    pass

class SignAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'text', 'authorized')

admin.site.register(NYMCImage, NYMCImageAdmin)
admin.site.register(Sign, SignAdmin)

