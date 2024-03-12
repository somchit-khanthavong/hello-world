from django.urls import path
from .views import *

urlpatterns = [
    path("", BlogPageView.as_view(), name="blogpage"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("add/", BlogCreateView.as_view(), name="blog_add"),
    path("<int:pk>/edit/", BlogUpdateView.as_view(), name="blog_edit"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
]