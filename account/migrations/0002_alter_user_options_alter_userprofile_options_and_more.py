# Generated by Django 4.2.11 on 2024-04-09 01:44

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='allergy',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='disease',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default='None', max_length=256),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='goals_calories',
            field=models.PositiveIntegerField(default=2500),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='goals_carb',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='goals_fat',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='goals_protein',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='height',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='medicine',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='weight',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.TextField(default='C:\\Users\\rlawl\\Desktop\\Capstone\\BigsasimiServer\\static/avatar/default-avatar.png'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='real_name',
            field=models.TextField(default='anonymous', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_uniq', to=settings.AUTH_USER_MODEL),
        ),
    ]
