# Generated by Django 5.0.2 on 2024-03-11 20:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0023_delete_likedposts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.category', verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_feed', models.TextField(blank=True, verbose_name='Отзыв')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_site.profile')),
            ],
        ),
    ]