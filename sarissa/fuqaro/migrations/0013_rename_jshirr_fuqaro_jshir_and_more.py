# Generated by Django 4.0.4 on 2022-05-08 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fuqaro', '0012_rename_jshir_fuqaro_jshir_takror_shir'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fuqaro',
            old_name='jshirr',
            new_name='jshir',
        ),
        migrations.RenameField(
            model_name='fuqaro_jshir_takror',
            old_name='shir',
            new_name='jshir',
        ),
    ]
