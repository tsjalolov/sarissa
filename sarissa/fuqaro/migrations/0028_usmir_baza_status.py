# Generated by Django 4.0.4 on 2022-05-15 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuqaro', '0027_alter_baza_fuqaro_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usmir',
            name='baza_status',
            field=models.BooleanField(default=False),
        ),
    ]
