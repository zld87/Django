# Generated by Django 3.0.4 on 2020-07-16 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vipapp01', '0008_top_register_user_update_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='top_user_group',
            name='describe',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]