# Generated by Django 4.1.5 on 2023-02-06 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="نام پست"
                    ),
                ),
                (
                    "english_title",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="نام پست به اینگلیسی",
                    ),
                ),
                ("slug", models.SlugField(blank=True, null=True, verbose_name="اسلاگ")),
                (
                    "image",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="blog/image",
                        verbose_name="عکس1",
                    ),
                ),
                (
                    "image2",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="blog/image",
                        verbose_name="عکس2",
                    ),
                ),
                (
                    "image3",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="blog/image",
                        verbose_name="عکس3",
                    ),
                ),
                (
                    "discription",
                    models.TextField(blank=True, null=True, verbose_name="توضیحات"),
                ),
                (
                    "content",
                    models.TextField(blank=True, null=True, verbose_name="بدنه پست"),
                ),
                (
                    "meta_title",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="نام دیگر"
                    ),
                ),
                (
                    "meta_content",
                    models.TextField(
                        blank=True, null=True, verbose_name="توضیحات بیشتر"
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="تهیه کننده پست",
                    ),
                ),
            ],
            options={
                "verbose_name": "وبلاگ",
                "verbose_name_plural": "تنضیمات قسمت وبلاگ",
                "ordering": ("-created",),
            },
        ),
    ]
