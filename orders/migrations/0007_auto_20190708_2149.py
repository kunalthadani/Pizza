# Generated by Django 2.0.3 on 2019-07-08 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.CharField(choices=[('Regular Pizza', ''), ('Sicilian Pizza', 'Sicilian Pizza'), ('Subs', 'Subs'), ('Pasta', 'Pasta'), ('Salad', 'Salad'), ('Dinner Platter', 'Dinner Platter')], max_length=64),
        ),
    ]