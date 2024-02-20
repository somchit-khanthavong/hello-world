from django.test import SimpleTestCase
from django.urls import reverse

class HomePageTests(SimpleTestCase):
    # ທົດສອບວ່າ URL ຂອງໜ້າເວັບຂອງເຮົາຖືກຕ້ອງບໍ່
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    # ທົດສອບຊື່ຂອງໜ້າເວັບຖືກຕ້ອງບໍ່
    def test_url_available_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    # ທົດສອບໄຟລ໌ template ທີ່ໃຊ້ຂອງແຕ່ລະໜ້າເວັບຖຶກຕ້ອງບໍ່
    def test_template_name_correct(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
    
class AboutPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
    def test_template_name_correct(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about.html')