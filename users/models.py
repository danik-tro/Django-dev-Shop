from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/%d',
                              blank=True,
                              verbose_name='Аватар пользователя')

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
