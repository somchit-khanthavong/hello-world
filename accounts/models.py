from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    # null ແມ່ນກ່ຽວຂ້ອງກັບ database / blank ແມ່ນກ່ຽວຂ້ອງກັບ form
    age = models.PositiveIntegerField(null=True, blank=True)