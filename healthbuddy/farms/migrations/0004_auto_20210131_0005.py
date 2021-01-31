# Generated by Django 3.1 on 2021-01-31 00:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('farms', '0003_auto_20210130_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babysitter',
            name='age',
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='babysitter',
            name='city',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='babysitter',
            name='communication',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='babysitter',
            name='experience',
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='babysitter',
            name='gender',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='babysitter',
            name='user_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gymmember',
            name='age',
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='gymmember',
            name='city',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='gymmember',
            name='communication',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gymmember',
            name='gender',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='gymmember',
            name='user_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='age',
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='city',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='communication',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='experience',
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='gender',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='user_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
