from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostTests(TestCase):
    @classmethod            # ສ້າງໂພດປອມເພື່ອທົດສອບລະບົບໂມເດວຖານຂໍ້ມູນ
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="ນີ້ແມ່ນການທົດສອບສ້າງໂພດ!!!!")
    
    def test_model_content(self):
        self.assertEqual(self.post.text, "ນີ້ແມ່ນການທົດສອບສ້າງໂພດ!!!!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse("postpage"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("postpage"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "postpage.html")

    # ທົດສອບແບບຫຼາຍໂຕໃນຟັງຊັນດຽວ
    def test_post(self):
        response = self.client.get(reverse("postpage"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ນີ້ແມ່ນການທົດສອບສ້າງໂພດ!!!!")
        self.assertTemplateUsed(response, "postpage.html")