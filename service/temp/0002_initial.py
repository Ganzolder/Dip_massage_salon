# Generated by Django 4.2.2 on 2024-06-26 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0001_initial"),
        ("service", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="services",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.course",
            ),
        ),
        migrations.AddField(
            model_name="apppointment",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="added_course",
                to="users.course",
                verbose_name="Курс",
            ),
        ),
        migrations.AddField(
            model_name="apppointment",
            name="masseur",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="masseur_surname",
                to="users.masseur",
                verbose_name="Массажист",
            ),
        ),
        migrations.AddField(
            model_name="apppointment",
            name="name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="client_name",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Имя клиента",
            ),
        ),
        migrations.AddField(
            model_name="apppointment",
            name="phone",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="client_phone",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Телефон клиента",
            ),
        ),
        migrations.AddField(
            model_name="apppointment",
            name="surname",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="client_surname",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Фамилия клиента",
            ),
        ),
    ]
