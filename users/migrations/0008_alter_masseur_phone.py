# Generated by Django 4.2.2 on 2024-06-29 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_masseur_description_masseur_phone_alter_masseur_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="masseur",
            name="phone",
            field=models.CharField(
                blank=True,
                help_text="Укажите телефон",
                max_length=35,
                null=True,
                verbose_name="Телефон",
            ),
        ),
    ]
