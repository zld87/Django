# Generated by Django 3.0.4 on 2020-09-15 10:38

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('vipapp01', '0011_auto_20200907_0205'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='interface_case',
            managers=[
                ('imanager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RenameField(
            model_name='interface_case',
            old_name='Assertion',
            new_name='assertion',
        ),
        migrations.AddField(
            model_name='function_case_content',
            name='function_Test_Case',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='vipapp01.Test_Case'),
        ),
        migrations.AddField(
            model_name='interface_case',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='interface_case',
            name='createuser',
            field=models.IntegerField(db_column='create_user', null=True),
        ),
        migrations.AddField(
            model_name='interface_case',
            name='data_type',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='interface_case',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='function_case_content',
            name='function_Preconditions',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='top_register_user',
            name='user',
            field=models.CharField(db_column='username', max_length=200, unique=True),
        ),
    ]