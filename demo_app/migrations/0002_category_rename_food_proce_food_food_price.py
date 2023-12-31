# Generated by Django 4.2.2 on 2023-07-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("demo_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("category_name", models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name="food",
            old_name="food_proce",
            new_name="food_price",
        ),
    ]
