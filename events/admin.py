from django.contrib import admin
from django.contrib.auth import get_user_model
from django.template.defaultfilters import pluralize
from django.utils.safestring import mark_safe
from .forms import EventAdminForm
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):

    form = EventAdminForm

    list_display = ('title', 'description', 'location', 'active', 'start', 'end', 'interest')
    list_filter = ('active', 'start')
    list_display_links = ('title',)
    search_fields = ('title', 'description')
    date_hierarchy = 'start'

    def interest(self, obj):
        return str(obj.reactions.count()) + " " + pluralize(obj.reactions.count(), 'User,Users')

    interest.short_description = 'Reacted by?'

    baton_cl_includes = [
        ('events/admin_include_top.html', 'top',),
    ]

    fieldsets = (
        ('Details', {
            'fields': ('title', 'location', 'description',),
            'classes': ('baton-tabs-init', 'baton-tab-fs-duration', 'baton-tab-group-fs-attachment',),
            'description': 'Details of event.'
        }),
        ('Time Frame', {
            'fields': ('start', 'end', ),
            'classes': ('tab-fs-duration', ),
            'description': 'Duration.'
        }),
        ('Attachment', {
            'fields': ('photo', ),
            'classes': ('tab-fs-attachment', ),
            'description': 'Add image.'
        }),
        ('Active', {
            'fields': ('active', ),
            'classes': ('tab-fs-none', ),
            # 'description': 'This is another description text'
        }),
    )



admin.site.register(Event, EventAdmin)