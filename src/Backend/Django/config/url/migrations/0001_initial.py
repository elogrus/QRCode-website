# Generated by Django 4.1.7 on 2023-02-18 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notable_links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Ссылка')),
            ],
        ),
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_url', models.IntegerField(verbose_name='Id ссылки')),
                ('email_author', models.EmailField(max_length=254, verbose_name='Email автора')),
                ('review', models.TextField(verbose_name='Отзыв')),
            ],
        ),
    ]