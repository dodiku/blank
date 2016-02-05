from django.contrib import admin
from blank.models import Post, UserProfile

class UserAdmin (admin.ModelAdmin):
    list_display = ('username')

class PostAdmin (admin.ModelAdmin):
    list_display = ('user', 'i_am', 'i_want', 'i_need', 'created', 'views', 'chats')

admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile)
