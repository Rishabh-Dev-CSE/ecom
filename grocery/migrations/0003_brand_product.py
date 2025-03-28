# Generated by Django 5.1.6 on 2025-02-25 12:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0002_alter_category_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, upload_to='brands')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Disable', 'Disable')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('mrp', models.CharField(max_length=100)),
                ('discount', models.IntegerField()),
                ('stock', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('images', models.ImageField(upload_to='Products')),
                ('description', models.TextField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery.category')),
            ],
        ),
    ]
