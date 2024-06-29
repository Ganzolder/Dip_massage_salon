# Generated by Django 4.2.2 on 2024-06-29 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0010_alter_user_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "permissions": [
                    ("change_activity", "Can block user"),
                    ("view_users", "Can view list of users"),
                    ("create_appointment", "Can create appointment"),
                    ("change_appointment", "Can change appointment"),
                    ("delete_appointment", "Can delete appointment"),
                    ("view_masseurs", "Can view list of masseurs"),
                    ("change_masseur", "Can delete appointment"),
                    ("create_masseur", "Can delete appointment"),
                    ("delete_masseur", "Can delete appointment"),
                    ("view_blog_posts", "Can view list of blog posts"),
                    ("change_blog_posts", "Can block blog posts"),
                    ("create_blog_posts", "Can create blog post"),
                    ("delete_blog_posts", "Can create blog post"),
                ],
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]
