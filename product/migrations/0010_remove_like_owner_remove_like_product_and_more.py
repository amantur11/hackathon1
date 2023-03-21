# Generated by Django 4.0.4 on 2023-03-17 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_rating_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='like',
            name='product',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='post',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
