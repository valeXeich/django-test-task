from django.test import TestCase, Client
from django.urls import reverse

from .models import CustomUser
from .forms import LoginForm


class Test(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(
            first_name='Sasuke',
            last_name='Uchiha',
            username='S.Uchiha',
            password='sharingan123',
            avatar='default.png'
        )
    
    def test_user_list_get(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context_data['users'][0], self.user)
        self.assertTemplateUsed(response, 'user_list.html')
    
    def test_login_get(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
    
    def test_login_form(self):
        data = {
            'username': self.user.username,
            'password': self.user.password
        }
        form = LoginForm(data=data)
        self.assertTrue(form.is_valid())
    


