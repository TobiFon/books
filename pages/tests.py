from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve

from .views import HomePageView

class HomePageTest(SimpleTestCase):
  def test_url_exist_at_correct_location(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    
  def test_hompepage_url_name(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    
  def test_homepage_template_used(self):
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'home.html')
    
  def test_homepage_contains_correct_html(self):
    response = self.client.get('/')
    self.assertContains(response, 'home page')
    
  def test_homepage_does_not_contains_correct_html(self):
    response = self.client.get('/')
    self.assertNotContains(response, 'this does not exist')
  
  def test_homepage_url_resolves_homepageview(self):
    view = resolve('/')
    self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

# Create your tests here.
