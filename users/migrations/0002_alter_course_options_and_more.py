# Generated by Django 4.2.2 on 2024-06-28 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="course",
            options={"verbose_name": "Курс", "verbose_name_plural": "Курсы"},
        ),
        migrations.RenameField(
            model_name="masseur",
            old_name="speciality",
            new_name="course",
        ),
    ]
