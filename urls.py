from django.urls import path
from . import views

urlpatterns = [
    # Home page
    # Requirement: / and /blog/ 
    path("", views.index, name="index"),

    # List of all blog posts
    # Requirement: /blog/blogs/ 
    path("blogs/", views.BlogPostListView.as_view(), name="blogs"),
    
    # Blog author (blogger) detail page
    # Requirement: /blog/blogger/<author-id> 
    path("blogger/<int:pk>/", views.BloggerDetailView.as_view(), name="blogger-details"),

    # Blog post detail page
    # Requirement: /blog/<blog-id> 
    path("<int:pk>/", views.BlogPostDetailView.as_view(), name="blog-details"),

    # List of all bloggers
    # Requirement: /blog/bloggers/ 
    path("bloggers/", views.BloggerListView.as_view(), name="bloggers"),
    
    # Comment form page
    # Requirement: /blog/<blog-id>/create 
    path("<int:pk>/create/", views.CommentCreateView.as_view(), name="comment-create"),
]