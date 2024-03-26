# Generated by Django 5.0.3 on 2024-03-22 16:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("price", models.FloatField()),
                ("stock", models.IntegerField()),
                ("image_url", models.CharField(max_length=2083)),
            ],
        ),
    ]
