# Generated by Django 4.0.4 on 2022-05-09 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuqaro', '0020_alter_usmir_guvohnoma_raqam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usmir',
            name='ism',
            field=models.CharField(max_length=200),
        ),
    ]