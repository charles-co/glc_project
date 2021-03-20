from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Audio, Video, Podcast, TV
from django.utils.translation import ugettext_lazy as _
import os.path

# Register your models here.

class AudioAdmin(admin.ModelAdmin):

    list_display = ('title', 'audio_file_player', 'created_at', 'updated_at')
    actions = ['custom_delete_selected']
    date_hierarchy = 'created_at'

    def custom_delete_selected(self, request, queryset):
        #custom delete code
        n = queryset.count()
        for i in queryset:
            # if i.audio_file:
            #     if os.path.exists(i.audio_file.path):
            #         os.remove(i.audio_file.path)
            i.delete()
        self.message_user(request, _("Successfully deleted %d audio files.") % n)
    custom_delete_selected.short_description = "Delete selected items"

    def get_actions(self, request):
        actions = super(AudioAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    baton_cl_includes = [
        ('contents/audio_admin_include_top.html', 'top',),
    ]

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    list_filter = ('created_at',)
    search_fields = ('title',)
    date_hierarchy = 'created_at'

    baton_cl_includes = [
        ('contents/video_admin_include_top.html', 'top',),
    ]

class PodcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at',)
    list_filter = ('created_at',)
    search_fields = ('title',)
    date_hierarchy = 'created_at'

    baton_cl_includes = [
        ('contents/podcast_admin_include_top.html', 'top',),
    ]

class TVAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'tv', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)
    
    def link(self, obj):
        return mark_safe("<a href='{}'>{}</a>".format(obj.url, obj.url))

    link.short_description = 'Link'
    
    baton_cl_includes = [
        ('contents/tv_admin_include_top.html', 'top',),
    ]
    
admin.site.register(Audio, AudioAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Podcast, PodcastAdmin)
admin.site.register(TV, TVAdmin)