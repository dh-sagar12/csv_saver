# Generated by Django 4.2.5 on 2023-09-15 06:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_alter_productimagemodel_images"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderdetailmodel",
            old_name="order_staus",
            new_name="order_status",
        ),
    ]
