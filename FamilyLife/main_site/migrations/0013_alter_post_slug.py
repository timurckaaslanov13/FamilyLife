# Generated by Django 5.0.2 on 2024-03-06 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0012_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(),
        ),
    ]
