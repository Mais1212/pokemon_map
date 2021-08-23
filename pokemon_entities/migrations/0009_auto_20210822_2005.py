# Generated by Django 3.1.13 on 2021-08-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_auto_20210821_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_en',
            field=models.CharField(default='', max_length=200, verbose_name='Заголовок на английском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_ja',
            field=models.CharField(default='', max_length=200, verbose_name='Заголовок на японском'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='title_ru',
            field=models.CharField(default='', max_length=200, verbose_name='Заголовок'),
        ),
    ]
