# Generated by Django 4.2.2 on 2024-06-28 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("service", "0004_apppointment_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apppointment",
            name="email",
            field=models.ForeignKey(
                default=9999,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Почта",
            ),
        ),
    ]
