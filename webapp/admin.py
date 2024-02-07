from django.contrib import admin
from .models import Post, User, Comment

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('post_id',)

admin.site.register(Post, PostAdmin)
admin.site.register(User)
admin.site.register(Comment)
