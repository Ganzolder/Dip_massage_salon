# Generated by Django 4.2.2 on 2024-06-28 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0002_rename_email_apppointment_creator"),
    ]

    operations = [
        migrations.AddField(
            model_name="apppointment",
            name="service",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="service.services",
                verbose_name="Массаж",
            ),
        ),
    ]