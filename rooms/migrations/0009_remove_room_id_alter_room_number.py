# Generated by Django 5.0.3 on 2024-03-31 09:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0008_remove_room_is_booked"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="room",
            name="id",
        ),
        migrations.AlterField(
            model_name="room",
            name="number",
            field=models.PositiveSmallIntegerField(
                primary_key=True, serialize=False, verbose_name="Номер"
            ),
        ),
    ]
