# Generated by Django 3.0.4 on 2020-11-09 09:51

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('vipapp01', '0014_auto_20201023_1747'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='interface_case',
            managers=[
                ('icaseManager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='interface_case',
            name='it_name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
