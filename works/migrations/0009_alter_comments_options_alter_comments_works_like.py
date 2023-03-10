# Generated by Django 4.1.5 on 2023-02-02 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("works", "0008_alter_comments_message"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comments",
            options={
                "ordering": ("-created",),
                "verbose_name": "نظر",
                "verbose_name_plural": "تنظیمات قسمت نظرات",
            },
        ),
        migrations.AlterField(
            model_name="comments",
            name="works",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comment",
                to="works.work",
                verbose_name="کار ها",
            ),
        ),
        migrations.CreateModel(
            name="Like",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "comments",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="likes2",
                        to="works.comments",
                        verbose_name="نظرات",
                    ),
                ),
                (
                    "users",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="likes2",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="کاربر",
                    ),
                ),
            ],
            options={
                "verbose_name": "لایک",
                "verbose_name_plural": "تنظیمات قسمت لایک ها",
                "ordering": ("-created",),
            },
        ),
    ]
