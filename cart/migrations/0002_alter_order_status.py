# Generated by Django 4.0.4 on 2023-03-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Decorated', 'Decorated'), ('Canceled', 'canceled')], default='New', max_length=20),
        ),
    ]