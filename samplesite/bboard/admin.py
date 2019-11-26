from django.contrib import admin

from .models import *

class BbAdmin (admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'image')
    list_display_links = ('title', 'content', 'image')
    search_fields = ('title', 'content')




admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
