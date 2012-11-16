from notyourmotleycrew.content.models import NYMCImage
from notyourmotleycrew.content.models import Sign
from notyourmotleycrew.content.models import Post

from django.contrib import admin

class NYMCImageAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'caption')
    list_filter = ('status',)

class SignAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'text', 'authorized')

class PostAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'title')

admin.site.register(NYMCImage, NYMCImageAdmin)
admin.site.register(Sign, SignAdmin)
admin.site.register(Post, PostAdmin)

