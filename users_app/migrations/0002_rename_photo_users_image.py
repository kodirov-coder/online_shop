# Generated by Django 3.2.13 on 2023-05-01 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='photo',
            new_name='image',
        ),
    ]