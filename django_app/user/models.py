from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    avatar = models.ImageField('Аватар', upload_to='user_avatar/')

    def __str__(self):
        return f'username: {self.username}'
