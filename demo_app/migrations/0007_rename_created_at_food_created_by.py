# Generated by Django 4.2.2 on 2023-07-15 15:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("demo_app", "0006_alter_food_created_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="food",
            old_name="created_at",
            new_name="created_by",
        ),
    ]
