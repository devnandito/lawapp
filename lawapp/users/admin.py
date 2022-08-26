from django.contrib import admin
from lawapp.users.models import Profile, User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username')
    search_fields = ('username',)
    list_filter = ('username',)
admin.site.register(User, UserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'description',)
    search_fields = ('description',)
    list_filter = ('description',)
admin.site.register(Profile, ProfileAdmin)