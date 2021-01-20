# Generated by Django 3.1.5 on 2021-01-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210119_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Способ доставки'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Способ доставки'),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]