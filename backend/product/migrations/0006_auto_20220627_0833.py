# Generated by Django 3.2 on 2022-06-27 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_sampleimages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attribute',
            old_name='description',
            new_name='description_tm',
        ),
        migrations.RenameField(
            model_name='attribute',
            old_name='title',
            new_name='title_tm',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='title_tm',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='description_tm',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='title_tm',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='description',
            new_name='description_tm',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='title',
            new_name='title_tm',
        ),
    ]
