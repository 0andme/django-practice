# Generated by Django 4.1.5 on 2023-01-17 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='이미지'),
        ),
    ]
