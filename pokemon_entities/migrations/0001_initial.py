from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=200, null=True)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_ja', models.CharField(max_length=200, null=True)),
                ('photo', models.ImageField(null=True, upload_to='')),
                ('description', models.TextField(null=True)),
                ('previous_evolution', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokemon_entities.pokemon')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('appeared_at', models.DateTimeField(null=True)),
                ('disappeared_at', models.DateTimeField(null=True)),
                ('lelvl', models.IntegerField(null=True)),
                ('health', models.IntegerField(null=True)),
                ('attack', models.IntegerField(null=True)),
                ('orotection', models.IntegerField(null=True)),
                ('endurance', models.IntegerField(null=True)),
                ('pokemon', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.pokemon')),
            ],
        ),
    ]
