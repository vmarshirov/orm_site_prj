# Generated by Django 4.1.7 on 2024-04-01 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0014_alter_item_item_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_nav_position',
            field=models.IntegerField(default=1, verbose_name='Приоритет в навигации (0 - исключить)'),
        ),
    ]
