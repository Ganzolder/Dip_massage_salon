from django.db import models
from django.contrib.auth.models import AbstractUser


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='e-mail', help_text='Введите почту')
    first_name = models.CharField(max_length=50, verbose_name='Имя', **NULLABLE, help_text='Введите имя')
    second_name = models.CharField(max_length=50, verbose_name='Фамилия', **NULLABLE, help_text='Введите фамилию')
    age = models.SmallIntegerField(verbose_name='Возраст', **NULLABLE, help_text='Введите возраст')
    avatar = models.ImageField(upload_to='user/avatar/', verbose_name='Аватар', **NULLABLE, help_text='Загрузите аватар')
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE, help_text='Введите телефон')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
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
                'view_blog_posts',
                'Can view list of blog posts'
            ),
            (
                'block_blog_posts',
                'Can block blog posts'
            ),
            (
                'create_blog_posts',
                'Can create blog post'
            )
        ]

        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Course(models.Model):
    title = models.CharField(max_length=50, verbose_name='Специализация', **NULLABLE, help_text='Укажите специализацию')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'


class Masseur(models.Model):
    name = models.CharField(max_length=35, verbose_name='Имя', help_text='Укажите имя')
    surname = models.CharField(max_length=75, verbose_name='Фамилия', help_text='Укажите фамилию')
    photo = models.ImageField(upload_to='user/masseur', verbose_name='Фото', **NULLABLE, help_text='Загрузите фото')
    speciality = models.ForeignKey(Course, on_delete=models.CASCADE, help_text='Укажите специализацию')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Массажист'
        verbose_name_plural = 'Массажисты'
