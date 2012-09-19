from notyourmotleycrew.content.models import NYMCImage

from django.contrib import admin

class NYMCImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(NYMCImage, NYMCImageAdmin)

