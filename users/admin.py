from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationForm


CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    form_add = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age']



admin.site.register(CustomUser, CustomUserAdmin)