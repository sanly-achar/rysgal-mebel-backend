# Generated by Django 3.2 on 2022-06-27 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20220627_0833'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserOrder',
            new_name='Order',
        ),
    ]
