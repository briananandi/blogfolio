from django.shortcuts import render, get_object_or_404
from .models import Blogger, BlogPost, Comment
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse

# Create your views here.

def index(request):
    num_bloggers = Blogger.objects.count()
    num_blog_posts = BlogPost.objects.count()
    num_comments = Comment.objects.count()

    context = {
        "num_bloggers": num_bloggers,
        "num_blog_posts": num_blog_posts,
        "num_comments": num_comments,
    }

    return render(request, "blog/index.html", context)

class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 5
    ordering = ["-post_date"]

class BlogPostDetailView(generic.DetailView):
    model = BlogPost

class BloggerListView(generic.ListView):
    model = Blogger

class BloggerDetailView(generic.DetailView):
    model = Blogger

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_posts'] = BlogPost.objects.filter(author=self.object).order_by('-post_date')
        return context

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["description"]
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.blog_post = get_object_or_404(BlogPost, pk=self.kwargs["pk"])
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = get_object_or_404(BlogPost, pk=self.kwargs["pk"])
        return context

    def get_success_url(self):
        return reverse("blog-details", args=[self.kwargs["pk"]]) 
    
