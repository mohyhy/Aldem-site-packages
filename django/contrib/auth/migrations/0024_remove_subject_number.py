# Generated by Django 5.0.6 on 2024-09-05 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0023_package_user_package'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='number',
        ),
    ]
