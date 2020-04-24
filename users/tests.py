from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignUpView

class UserModelTest(TestCase):

    def setUp(self):
        self.User = get_user_model()

    def test_create_user(self):
        user = self.User.objects.create_user(
            username='testuser',
            email = 'testuser@gmail.com',
            password = 'password'
        )

        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        user = self.User.objects.create_superuser(
            username='testsuperuser',
            email = 'testsuperuser@gmail.com',
            password = 'password'
        )

        self.assertEqual(user.username, 'testsuperuser')
        self.assertEqual(user.email, 'testsuperuser@gmail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignUpTest(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'signup')
        self.assertNotContains(self.response, 'this is homepage')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_resolve_view(self):
        view = resolve(reverse('signup'))
        self.assertEqual(
            view.func.__name__,
            SignUpView.as_view().__name__
        )