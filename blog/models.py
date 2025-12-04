from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Blogger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(help_text="Add brief bio here.")

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("blogger-details", args=[str(self.id)])
    
    class Meta:
        ordering = ["user__username"]
        verbose_name = "Blogger"
        verbose_name_plural = "Bloggers"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog-details", args=[str(self.id)])
    
    class Meta:
        ordering = ["-post_date"]
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments")
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description[:75]
    
    class Meta:
        ordering = ["post_date"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"