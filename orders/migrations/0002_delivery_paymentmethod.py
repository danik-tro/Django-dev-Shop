# Generated by Django 3.1.5 on 2021-01-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Способ доставки')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Способ доставки',
                'verbose_name_plural': 'Способы доставки',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Способ доставки')),
                ('slug', models.SlugField()),
            ],
        ),
    ]
