# Generated by Django 4.1.5 on 2023-01-19 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_product_comment_aaaa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='aaaa',
            new_name='product',
        ),
    ]