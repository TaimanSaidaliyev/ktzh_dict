# Generated by Django 5.1 on 2024-08-28 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0011_alter_division_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='division',
            options={'ordering': ['serial_number'], 'verbose_name': 'Отдел', 'verbose_name_plural': 'Отделы'},
        ),
        migrations.AlterUniqueTogether(
            name='division',
            unique_together={('serial_number',)},
        ),
    ]
