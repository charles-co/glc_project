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
    pass

# admin.site.register(Bible, BibleAdmin)
# admin.site.register(Book, BookAdmin)
# admin.site.register(Chapter, ChapterAdmin)
# admin.site.register(Verse, VerseAdmin)
admin.site.register(TodaysVerse, TodaysVerseAdmin)