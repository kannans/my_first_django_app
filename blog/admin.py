from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'author', 'publish', 'status')
  list_filter = ('created', 'author', 'publish', 'status')
  search_fields = ('title', 'body')
  prepopulated_fields = { 'slug': ('title',) }
  row_id_fields = ('author',)
  ordering = ["status", "publish"]

admin.site.register(Post, PostAdmin)
