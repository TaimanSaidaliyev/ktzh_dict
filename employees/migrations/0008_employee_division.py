# Generated by Django 5.1 on 2024-08-27 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0007_alter_division_serial_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.division', verbose_name='Отдел'),
        ),
    ]
