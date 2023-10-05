# Generated by Django 4.2.5 on 2023-09-15 04:32

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bannerimagesmodel",
            name="banner_image",
            field=models.ImageField(
                db_column="banner_image",
                upload_to=home.models.BannerImagesModel.banner_directory_path,
            ),
        ),
    ]
