from django import forms
from django.contrib.auth.forms import UserCreationForm
from fuqaro_uchot.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = "__all__"
