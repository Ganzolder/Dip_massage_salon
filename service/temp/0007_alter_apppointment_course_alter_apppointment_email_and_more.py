# Generated by Django 4.2.2 on 2024-06-28 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0004_user_enabled_user_token"),
        ("service", "0006_alter_apppointment_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apppointment",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.course",
                verbose_name="Курс",
            ),
        ),
        migrations.AlterField(
            model_name="apppointment",
            name="email",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Почта",
            ),
        ),
        migrations.AlterField(
            model_name="apppointment",
            name="masseur",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.masseur",
                verbose_name="Массажист",
            ),
        ),
        migrations.AlterField(
            model_name="apppointment",
            name="name",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Имя клиента"
            ),
        ),
        migrations.AlterField(
            model_name="apppointment",
            name="phone",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Телефон клиента"
            ),
        ),
        migrations.AlterField(
            model_name="apppointment",
            name="surname",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Фамилия клиента"
            ),
        ),
    ]