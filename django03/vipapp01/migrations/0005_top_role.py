# Generated by Django 3.0.4 on 2020-05-19 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vipapp01', '0004_auto_20200514_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Top_Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=100)),
                ('role_user', models.ManyToManyField(to='vipapp01.Top_Register_User')),
            ],
        ),
    ]
