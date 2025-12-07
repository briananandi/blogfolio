from django.contrib import admin

# Register your models here.

from .models import Blogger, BlogPost, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "post_date")
    # list_filter = ("post_date", "author")
    # search_fields = ("title", "content", "author__name")
    inlines = [CommentInline]

class BloggerAdmin(admin.ModelAdmin):
    list_display = ("user", "bio")
    # search_fields = ("user", "user__username")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("description", "post_date", "user", "blog_post")

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Blogger, BloggerAdmin)
admin.site.register(Comment, CommentAdmin)

