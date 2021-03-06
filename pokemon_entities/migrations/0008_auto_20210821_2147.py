from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_auto_20210821_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='attack',
            field=models.IntegerField(blank=True, null=True, verbose_name='Сила атаки'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='endurance',
            field=models.IntegerField(blank=True, null=True, verbose_name='Выносливость'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(blank=True, null=True, verbose_name='Здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lelvl',
            field=models.IntegerField(blank=True, null=True, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='orotection',
            field=models.IntegerField(blank=True, null=True, verbose_name='Защита'),
        ),
    ]
