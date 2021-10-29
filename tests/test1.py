from unittest import TestCase
from app import main

class TryTesting(TestCase):
    def setUp(self):
        self.apps = main.create_app()
        self.apps.config['TESTING'] = True
        self.client = self.apps.test_client()
        self.payload = {'its': 'empty'}


    def test_health(self):
        response = self.client.get('/health')
        self.assertEqual(response.data,  b'Healthy')
        self.assertEqual(response.status_code, 400)
        
        
    def test_404(self):
        response = self.client.get('/healths')

        expected_resp = {
            'error': '404 Not Found: The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.'
            }

        self.assertEqual(response.get_json(), expected_resp)
        self.assertEqual(response.status_code, 404)

    def test_home(self):
        response = self.client.get('/')

        self.assertEqual(response.data,  b'This is a test app')
        self.assertEqual(response.status_code, 200)
        
        