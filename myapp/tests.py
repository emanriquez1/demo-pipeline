from django.test import TestCase, Client

# Create your tests here.
class PingTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_endpoint_ping_responde_ping_pong(self):
        response = self.client.get('/ping/')
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {'ping': 'pang'})