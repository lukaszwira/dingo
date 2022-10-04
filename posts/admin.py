from django.contrib import admin
from posts.models import Post, Author

# Register your models here.

class PostsAdmin(admin.ModelAdmin):
   list_display = ["id", "author", "title", "content", "created", "modified"]
   list_filter = ["author"]
   search_fields = ["title"]

admin.site.register(Post, PostsAdmin)

class AuthorAdmin(admin.ModelAdmin):
   list_display = ["nick", "email"]

admin.site.register(Author, AuthorAdmin)
