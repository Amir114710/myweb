# Generated by Django 4.1.5 on 2023-01-31 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("works", "0004_rename_image1_work_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="work",
            name="detail",
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]