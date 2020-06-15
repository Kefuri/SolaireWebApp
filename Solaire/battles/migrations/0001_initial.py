# Generated by Django 3.0.6 on 2020-06-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monster_type', models.CharField(max_length=15)),
                ('attack', models.IntegerField(max_length=5)),
                ('defense', models.IntegerField(max_length=5)),
                ('speed', models.IntegerField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('move_type', models.CharField(max_length=15)),
                ('damage', models.IntegerField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=15)),
                ('monsters', models.ManyToManyField(to='battles.Monster')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('elo', models.IntegerField(max_length=5)),
                ('teams', models.ManyToManyField(to='battles.Team')),
            ],
        ),
        migrations.AddField(
            model_name='monster',
            name='moves',
            field=models.ManyToManyField(to='battles.Move'),
        ),
    ]
