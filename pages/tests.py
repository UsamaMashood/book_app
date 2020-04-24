from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView

class HomePageTest(TestCase):
    
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'home.html')
        self.assertContains(self.response, 'HOMEPAGE')
        self.assertNotContains(self.response, 'this is homepage')

    def test_homepage_resolve_view(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__ ,
            HomePageView.as_view().__name__

        )