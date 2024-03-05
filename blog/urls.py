from django.urls import path
from .views import BlogPageView, BlogDetailView


urlpatterns = [
    path("", BlogPageView.as_view(), name="blogpage"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
]