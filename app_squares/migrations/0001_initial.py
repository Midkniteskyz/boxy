# Generated by Django 3.2.6 on 2021-08-18 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_nfl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('cellStatus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Square',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardStatus', models.BooleanField(default=False)),
                ('team_x', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='TeamX', to='app_nfl.team')),
                ('team_y', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='TeamY', to='app_nfl.team')),
            ],
        ),
    ]
