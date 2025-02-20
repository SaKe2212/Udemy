from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Feedback, Product



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','birth_date','bio']


from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput)



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content', 'rating']

class ProductForm(forms.ModelForm):
    videos = forms.FileField(widget=forms.FileInput(), required=False)    
    
    class Meta:
        model = Product
        fields = ['name',  'price', 'description','images', ]

class LogoutForm(forms.ModelForm):
    pass
