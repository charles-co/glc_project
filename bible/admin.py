from django.contrib import admin
from .models import Bible, Book, Chapter, Verse, TodaysVerse
# Register your models here.

class BibleAdmin(admin.ModelAdmin):
    pass

class BookAdmin(admin.ModelAdmin):
    pass

class ChapterAdmin(admin.ModelAdmin):
    pass

class VerseAdmin(admin.ModelAdmin):
    pass

class TodaysVerseAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'bible_verse', 'message']
    readonly_fields = ['message',]
    search_fields = ('title', 'message')
    date_hierarchy = 'date'
    list_select_related = (
        'verse',
        'bible',
    )

    def bible_verse(self, obj):
        return "{} ({})".format(obj.verse.reference, obj.bible.abbreviation)

    bible_verse.short_description = 'Bible Verse'

    baton_cl_includes = [
        ('bible/admin_include_top.html', 'top',),
    ]

# admin.site.register(Bible, BibleAdmin)
# admin.site.register(Book, BookAdmin)
# admin.site.register(Chapter, ChapterAdmin)
# admin.site.register(Verse, VerseAdmin)
admin.site.register(TodaysVerse, TodaysVerseAdmin)