# Generated by Django 4.1.7 on 2023-02-25 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_abc_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abc',
            name='c',
            field=models.IntegerField(choices=[(0, 'ноль'), (10, 'десять'), (15, 'пятнадцать'), (20, 'двадцать')], default=0, verbose_name='Значение С'),
        ),
    ]
