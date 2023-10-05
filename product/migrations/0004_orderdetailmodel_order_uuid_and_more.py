# Generated by Django 4.2.5 on 2023-09-18 04:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_rename_order_staus_orderdetailmodel_order_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderdetailmodel",
            name="order_uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name="productimagemodel",
            name="product_id",
            field=models.ForeignKey(
                db_column="product_id",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="product.productmodel",
            ),
        ),
    ]
