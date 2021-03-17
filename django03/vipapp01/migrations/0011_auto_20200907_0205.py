# Generated by Django 3.0.4 on 2020-09-07 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vipapp01', '0010_auto_20200904_0336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test_plan',
            name='plan_case',
        ),
        migrations.AlterField(
            model_name='interface_case',
            name='state',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='test_case',
            name='case_priority',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='test_case',
            name='case_result',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='test_case',
            name='case_type',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='test_case',
            name='test_mode',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='test_plan',
            name='phase',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='test_plan',
            name='plan_state',
            field=models.IntegerField(default=1),
        ),
    ]