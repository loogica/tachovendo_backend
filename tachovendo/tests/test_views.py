from django.test import TestCase
from django.core.urlresolvers import reverse

class HomeViewTest(TestCase):
    def test_get_home(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_info(self):
        response = self.client.get(reverse('rain_info'))
        self.assertEquals(response.status_code, 200)
