# Generated by Django 4.2.2 on 2024-06-26 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Apppointment",
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
                    "date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата и время записи"
                    ),
                ),
            ],
            options={
                "verbose_name": "Запись на массаж",
                "verbose_name_plural": "Записи на массаж",
            },
        ),
        migrations.CreateModel(
            name="Services",
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
                        max_length=100, unique=True, verbose_name="Название"
                    ),
                ),
                (
                    "content",
                    models.TextField(blank=True, null=True, verbose_name="Содержимое"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="services/images/",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "icon",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="services/icons/",
                        verbose_name="Иконка",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="Стоимость",
                    ),
                ),
            ],
            options={
                "verbose_name": "Услуга",
                "verbose_name_plural": "Услуги",
            },
        ),
    ]
