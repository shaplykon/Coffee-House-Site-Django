from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_about_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
