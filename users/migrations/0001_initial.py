# Generated by Django 4.2.2 on 2024-06-26 19:49

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        help_text="Укажите курс",
                        max_length=50,
                        null=True,
                        verbose_name="Курс",
                    ),
                ),
            ],
            options={
                "verbose_name": "Специализация",
                "verbose_name_plural": "Специализации",
            },
        ),
        migrations.CreateModel(
            name="Masseur",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Укажите имя", max_length=35, verbose_name="Имя"
                    ),
                ),
                (
                    "surname",
                    models.CharField(
                        help_text="Укажите фамилию",
                        max_length=75,
                        verbose_name="Фамилия",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото",
                        null=True,
                        upload_to="user/masseur",
                        verbose_name="Фото",
                    ),
                ),
                (
                    "speciality",
                    models.ForeignKey(
                        help_text="Укажите специализацию",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.course",
                    ),
                ),
            ],
            options={
                "verbose_name": "Массажист",
                "verbose_name_plural": "Массажисты",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Введите почту",
                        max_length=254,
                        unique=True,
                        verbose_name="e-mail",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True,
                        help_text="Введите имя",
                        max_length=50,
                        null=True,
                        verbose_name="Имя",
                    ),
                ),
                (
                    "second_name",
                    models.CharField(
                        blank=True,
                        help_text="Введите фамилию",
                        max_length=50,
                        null=True,
                        verbose_name="Фамилия",
                    ),
                ),
                (
                    "age",
                    models.SmallIntegerField(
                        blank=True,
                        help_text="Введите возраст",
                        null=True,
                        verbose_name="Возраст",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите аватар",
                        null=True,
                        upload_to="user/avatar/",
                        verbose_name="Аватар",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        help_text="Введите телефон",
                        max_length=35,
                        null=True,
                        verbose_name="Телефон",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
                "permissions": [
                    ("change_activity", "Can block user"),
                    ("view_users", "Can view list of users"),
                    ("create_appointment", "Can create appointment"),
                    ("change_appointment", "Can change appointment"),
                    ("delete_appointment", "Can delete appointment"),
                    ("view_blog_posts", "Can view list of blog posts"),
                    ("block_blog_posts", "Can block blog posts"),
                    ("create_blog_posts", "Can create blog post"),
                ],
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
