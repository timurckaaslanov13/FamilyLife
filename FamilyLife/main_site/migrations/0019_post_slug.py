# Generated by Django 5.0.2 on 2024-03-07 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0018_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
