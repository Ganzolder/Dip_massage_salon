from django.db import models
from django.contrib.auth.models import AbstractUser


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='e-mail', help_text='Введите почту')
    first_name = models.CharField(max_length=50, verbose_name='Имя', **NULLABLE, help_text='Введите имя')
    second_name = models.CharField(max_length=50, verbose_name='Фамилия', **NULLABLE, help_text='Введите фамилию')
    age = models.SmallIntegerField(verbose_name='Возраст', **NULLABLE, help_text='Введите возраст')
    avatar = models.ImageField(
        upload_to='user/avatar/', verbose_name='Аватар', **NULLABLE, help_text='Загрузите аватар')
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE, help_text='Введите телефон')
    enabled = models.BooleanField(default=True, verbose_name='Активен')
    token = models.CharField(max_length=100, verbose_name="Token", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:

        verbose_name = 'Пользователь'
        permissions = [
            (
                'change_activity',
                'Can block user'
            ),
            (
                'view_users',
                'Can view list of users'
            ),
            (
                'view_admin_list_app',
                'Can view all appointments'
            ),
            (
                'create_appointment',
                'Can create appointment'
            ),
            (
                'change_appointment',
                'Can change appointment'
            ),
            (
                'delete_appointment',
                'Can delete appointment'
            ),
            (
                'view_masseurs',
                'Can view list of masseurs'
            ),
            (
                'change_masseur',
                'Can delete masseur'
            ),
            (
                'create_masseur',
                'Can delete masseur'
            ),
            (
                'delete_masseur',
                'Can delete masseur'
            ),
            (
                'view_blog_posts',
                'Can view list of blog posts'
            ),
            (
                'change_blog_posts',
                'Can block blog posts'
            ),
            (
                'create_blog_posts',
                'Can create blog post'
            ),
            (
                'delete_blog_posts',
                'Can create blog post'
            ),
            (
                'view_services',
                'Can view list of services'
            ),
            (
                'change_services',
                'Can block services'
            ),
            (
                'create_services',
                'Can create services'
            ),
            (
                'delete_services',
                'Can create services'
            )
        ]
        verbose_name_plural = 'Пользователи'


class Masseur(models.Model):
    name = models.CharField(max_length=35, verbose_name='Имя', help_text='Укажите имя', **NULLABLE)
    surname = models.CharField(max_length=75, verbose_name='Фамилия', help_text='Укажите фамилию', **NULLABLE)
    description = models.TextField(
        max_length=1000, verbose_name='О массажисте', help_text='Напишите что-нибудь', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Телефон', help_text='Укажите телефон', **NULLABLE)
    photo = models.ImageField(upload_to='user/masseur/', verbose_name='Фото', **NULLABLE, help_text='Загрузите фото')
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Массажист'
        verbose_name_plural = 'Массажисты'
