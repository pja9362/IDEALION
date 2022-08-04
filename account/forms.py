from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'nickname']


class editProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'nickname', 'lat', 'lng']

