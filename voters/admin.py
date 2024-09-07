from django.contrib import admin
from .models import Voter
from django.utils.html import format_html


admin.site.site_header = "UMCC VOTER REGISTER"  # Header on the admin pages
admin.site.site_title = "UMCC VOTER REGISTER"  # Title in the browser tab
admin.site.index_title = "Welcome to UMCC VOTER REGISTER Dashboard"  # Title on the dashboard


class VoterAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'registered_by', 'registered_at', 'has_voted')
    list_filter = ('registered_by', 'registered_at', 'has_voted')
    search_fields = ('name', 'registered_by__username')
    readonly_fields = ('image_tag', 'registered_at')

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))

    image_tag.short_description = 'Image'


admin.site.register(Voter, VoterAdmin)
