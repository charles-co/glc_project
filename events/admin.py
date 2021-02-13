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
    search_fields = ('title',)
    date_hierarchy = 'start'
    # readonly_fields = ["photo_image"]


    def interest(self, obj):
        return str(obj.reactions.count()) + " " + pluralize(obj.reactions.count(), 'User,Users')

    interest.short_description = 'Reacted by?'

    # def photo_image(self, obj):
    #     if obj != "":
    #         return mark_safe('<img src="{url}" width="100%" height="50" />'.format(
    #             url = obj.photo.url,
    #             width=obj.photo.width,
    #             height=obj.photo.height,
    #             )
    #         )
    #     return mark_safe('<p>No image uploaded yet, please save & check back.</p>')



admin.site.register(Event, EventAdmin)