from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# ກຳນົດຄ່າແບບຟອມສ້າງບັນຊີຕັ້ງຕົ້ນໃຫ້ເພີ່ມໂມເດວທີ່ເຮົາສ້າງເອງເຂົ້າໄປ
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)

# ທຳການປ່ຽນແປງແບບຟອມໃຫ້ເປັນແບບໃໝ່
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields