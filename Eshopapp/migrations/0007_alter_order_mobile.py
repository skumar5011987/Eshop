# Generated by Django 4.0.6 on 2022-08-21 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshopapp', '0006_alter_order_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='mobile',
            field=models.CharField(max_length=150),
        ),
    ]
