# Generated by Django 5.1 on 2024-08-27 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_department_serial_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='serial_number',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Порядковый номер'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='serial_number',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Порядковый номер'),
        ),
        migrations.AlterField(
            model_name='employeestatus',
            name='serial_number',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Порядковый номер'),
        ),
        migrations.AlterField(
            model_name='position',
            name='serial_number',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Порядковый номер'),
        ),
    ]
