from django.contrib import admin
from lawapp.levels.models import Level

class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'description',)
    search_fields = ('description',)
    list_filter = ('description',)
admin.site.register(Level, LevelAdmin)