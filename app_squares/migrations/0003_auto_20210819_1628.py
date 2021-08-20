# Generated by Django 3.2.6 on 2021-08-19 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_nfl', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_squares', '0002_cell_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cell',
            name='square',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='cells', to='app_squares.square'),
        ),
        migrations.AlterField(
            model_name='cell',
            name='user',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='square',
            name='team_x',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='teamx', to='app_nfl.team'),
        ),
        migrations.AlterField(
            model_name='square',
            name='team_y',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='teamy', to='app_nfl.team'),
        ),
    ]