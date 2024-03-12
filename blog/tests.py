from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import BlogPost
from django.urls import reverse
# Create your tests her

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", 
            email="0Vw5k@example.com", 
            password = "secret"
        )

        cls.blogpost = BlogPost.objects.create(
            title="A good title",
            content="Nice body content",
            author=cls.user,
        )
    
    def test_blog_post_model(self):
        self.assertEqual(self.blogpost.title, "A good title")
        self.assertEqual(self.blogpost.content, "Nice body content")
        self.assertEqual(str(self.blogpost), "A good title")
        self.assertEqual(self.blogpost.author.username, "testuser")
        self.assertEqual(self.blogpost.get_absolute_url(), "/blog/1/")

    def test_blog_post_create(self):
        response = self.client.post(
            reverse("blog_add"), {
                "title": "New title",
                "author": self.user.id,
                "content": "New text"
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogPost.objects.last().title, "New title")
        self.assertEqual(BlogPost.objects.last().content, "New text")

    def test_blog_post_updateview(self): 
        response = self.client.post(
            reverse("blog_edit", args="1"),
            {
                "title": "Updated title",
                "content": "Updated text",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogPost.objects.last().title, "Updated title")
        self.assertEqual(BlogPost.objects.last().content, "Updated text")

    def test_blog_post_deleteview(self): 
        response = self.client.post(reverse("blog_delete", args="1"))
        self.assertEqual(response.status_code, 302)