# Generated by Django 4.0.6 on 2022-08-21 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshopapp', '0007_alter_order_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.IntegerField(max_length=150),
        ),
    ]
