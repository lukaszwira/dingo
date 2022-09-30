from django.contrib import admin
from maths.models import Math, Result
from posts.models import Post
# Register your models here.

class MathAdmin(admin.ModelAdmin):
   list_display = ["id", "operation", "a", "b", "created", "result"]
   list_filter = ["operation"]
   search_fields = ["a", "b"]

admin.site.register(Math, MathAdmin)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
   list_display = ['id', 'value', 'error']


class PostsAdmin(admin.ModelAdmin):
   list_display = ["id", "author", "title", "content", "created", "modified"]
   list_filter = ["author"]
   search_fields = ["title"]

admin.site.register(Post, PostsAdmin)
