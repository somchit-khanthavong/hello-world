from django.views.generic import ListView, DetailView
from django.views.generic.edit import *
from django.urls import reverse_lazy
from .models import BlogPost

class BlogPageView(ListView):
    model = BlogPost
    template_name = "blogpage.html"

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog_detail.html"

class BlogCreateView(CreateView):
    model = BlogPost
    template_name = "blog_add.html"
    fields = ["title", "author", "content"]
    success_url = reverse_lazy("blogpage")

class BlogUpdateView(UpdateView):
    model = BlogPost
    template_name = "blog_edit.html"
    fields = ["title", "content"]

class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog_delete.html"
    success_url = reverse_lazy("blogpage")