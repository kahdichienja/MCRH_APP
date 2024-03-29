# Generated by Django 2.1.7 on 2019-08-15 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('searches', '0003_auto_20190815_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchquery',
            name='child',
        ),
        migrations.AddField(
            model_name='searchquery',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='searchquery',
            name='query',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]
