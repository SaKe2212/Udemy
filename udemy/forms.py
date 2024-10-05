# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# #
# # class SignUpForm(UserCreationForm):
# #     email = forms.EmailField()
# #
# #     class Meta:
# #         model = User
# #         fields = ['username', 'email', 'password1', 'password2']
#
# from django.contrib.auth.forms import UserCreationForm
# from .models import CustomUser  # Импорт вашей кастомной модели
#
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser  # Используйте кастомную модель здесь
#         fields = ('username', 'email', 'password1', 'password2')

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Импорт вашей кастомной модели

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser  # Используйте кастомную модель
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
