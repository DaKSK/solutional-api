# Generated by Django 4.0 on 2022-01-04 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_order_options_alter_orderitem_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-id',)},
        ),
    ]
