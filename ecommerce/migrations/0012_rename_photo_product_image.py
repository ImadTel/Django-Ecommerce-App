# Generated by Django 3.2 on 2021-08-05 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0011_product_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='photo',
            new_name='image',
        ),
    ]