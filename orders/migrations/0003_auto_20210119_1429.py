# Generated by Django 3.1.5 on 2021-01-19 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_delivery_paymentmethod'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paymentmethod',
            options={'ordering': ('name',), 'verbose_name': 'Способ оплаты', 'verbose_name_plural': 'Способы оплаты'},
        ),
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='orders.delivery'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='orders.paymentmethod'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='delivery',
            name='name',
            field=models.CharField(default='-', max_length=50, verbose_name='Способ доставки'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='slug',
            field=models.SlugField(default='-'),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='name',
            field=models.CharField(default='-', max_length=50, verbose_name='Способ доставки'),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='slug',
            field=models.SlugField(default='-'),
        ),
    ]
