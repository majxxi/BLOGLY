from app import app
from unittest import TestCase

class RouteTestCase(TestCase):
    """ Test cases for routes in app.py """

    def setUp(self): 
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_user_list(self):
        res = self.client.get('/users')
        html = res.get_data(as_text=True)

        self.assertEqual(res.status_code, 200)
        self.assertIn('<h1>Blogly Users</h1>', html)
    
    def test_index_redirect(self):
        res = self.client.get('/')
        html = res.get_data(as_text=True)

        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.location, 'http://localhost/users')

    def test_create_new(self):
        res = self.client.get('/users/new')
        html = res.get_data(as_text=True)

        self.assertEqual(res.status_code, 200)
        self.assertIn('<h1>Create a user</h1>', html)

    def test_create_new_post(self):
        res = self.client.post('/users/new', data={'first_name': 'felix', 'last_name': 'miroh', 'image_url': 'google.com'})
        html = res.get_data(as_text=True)

        self.assertEqual(res.status_code, 302)
        self.assertEqual(res.location, 'http://localhost/users')


        


        
