# Generated by Django 3.0.4 on 2020-05-14 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vipapp01', '0003_auto_20200513_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='top_register_user',
            name='userphone',
            field=models.CharField(blank=True, db_column='phone', max_length=100, null=True),
        ),
    ]
