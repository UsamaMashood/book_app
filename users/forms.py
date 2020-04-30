from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from allauth.account.forms import SignupForm
from django import forms



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name' ,'email', 'username','age')


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name' ,'email', 'username','age')

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30,strip=True, required=True)
    last_name = forms.CharField(max_length=30, strip=True, required=True)
    age = forms.IntegerField(min_value=18, max_value=100, required=True)

    def signup(self, request, user):

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.age = self.cleaned_data['age']
        user.save()

        return user

