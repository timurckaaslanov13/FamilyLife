# Generated by Django 5.0.2 on 2024-03-06 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0002_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
