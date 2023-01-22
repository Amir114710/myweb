# Generated by Django 4.1.4 on 2023-01-22 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Activity",
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
                ("image", models.ImageField(upload_to="about/actitvity_image")),
                ("content", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="About",
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
                ("about_content", models.TextField()),
                (
                    "activity",
                    models.ManyToManyField(
                        related_name="actitvities", to="home_app.activity"
                    ),
                ),
            ],
        ),
    ]
