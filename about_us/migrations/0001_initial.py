# Generated by Django 4.0.4 on 2023-03-03 14:34

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('text', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Наши преимущества',
                'verbose_name_plural': 'Наши преимущества',
            },
        ),
        migrations.CreateModel(
            name='FooterOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('text', models.TextField()),
                ('number', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='HelpImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Помощь',
                'verbose_name_plural': 'Помощь',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Публичная оферта',
                'verbose_name_plural': 'Публичная оферта',
            },
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('help', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about_us.helpimages')),
            ],
            options={
                'verbose_name': 'Помощь',
                'verbose_name_plural': 'Помощь',
            },
        ),
        migrations.CreateModel(
            name='FooterTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Number', 'Number'), ('Mail', 'Mail'), ('Instagram', 'Instagram'), ('Telegram', 'Telegram'), ('WhatsApp', 'WhatsApp')], max_length=100)),
                ('network', models.CharField(max_length=30)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('footer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about_us.footerone')),
            ],
        ),
        migrations.CreateModel(
            name='AboutImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_image', to='about_us.about')),
            ],
        ),
    ]
