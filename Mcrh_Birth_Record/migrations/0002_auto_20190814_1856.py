# Generated by Django 2.1.7 on 2019-08-14 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mcrh_Birth_Record', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mcrh_Birth_Record.Parent', verbose_name='notified_id'),
        ),
    ]
