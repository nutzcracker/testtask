# Generated by Django 4.0.6 on 2024-01-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='product',
            field=models.JSONField(default=dict),
        ),
    ]
