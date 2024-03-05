from django.views.generic import ListView, DetailView
from .models import BlogPost

class BlogPageView(ListView):
    model = BlogPost
    template_name = "blogpage.html"

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog_detail.html"