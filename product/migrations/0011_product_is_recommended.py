# Generated by Django 4.0.4 on 2023-03-19 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_remove_like_owner_remove_like_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_recommended',
            field=models.BooleanField(default=False),
        ),
    ]
