# Generated by Django 4.0.6 on 2024-01-29 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_alter_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='product',
            new_name='products',
        ),
    ]
