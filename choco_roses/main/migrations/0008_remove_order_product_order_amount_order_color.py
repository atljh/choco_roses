# Generated by Django 4.0.6 on 2022-07-28 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_order_amount_remove_order_color_order_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.roseamount'),
        ),
        migrations.AddField(
            model_name='order',
            name='color',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.rosecolor'),
        ),
    ]
