# Generated by Django 3.0.4 on 2020-05-13 08:08

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Top_User_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(db_column='groupname', max_length=200)),
                ('group_state', models.BooleanField(db_column='state', default=False)),
                ('group_create', models.DateTimeField(auto_now_add=True, db_column='create_time')),
                ('group_update', models.DateTimeField(auto_now=True, db_column='update_time')),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'top_user_group',
            },
        ),
        migrations.CreateModel(
            name='Top_Register_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(db_column='username', max_length=200)),
                ('pwd', models.CharField(db_column='password', max_length=200)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('isdelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'top_register_user',
            },
            managers=[
                ('userManager', django.db.models.manager.Manager()),
            ],
        ),
    ]