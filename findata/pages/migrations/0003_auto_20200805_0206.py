# Generated by Django 3.0.6 on 2020-08-05 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200805_0047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticker',
            old_name='ticker',
            new_name='symbol',
        ),
    ]
