# Generated by Django 4.1.7 on 2023-04-17 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0006_alter_item_item_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('-item_nav_position',), 'verbose_name': 'Содержание главного фрагмента', 'verbose_name_plural': 'Содержание главных фрагментов страниц'},
        ),
    ]
