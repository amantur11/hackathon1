# Generated by Django 4.0.4 on 2023-03-03 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=30)),
                ('Country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('data', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('Decorated', 'Decorated'), ('Сanceled', 'Сanceled')], default='New', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.imageproducts')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.order')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('quantity_in_line', models.IntegerField()),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.order')),
            ],
        ),
    ]
