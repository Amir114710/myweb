# Generated by Django 4.1.4 on 2023-01-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("email", models.EmailField(max_length=255, verbose_name="ادرس ایمیل")),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=13, null=True, verbose_name="شماره تلفن"
                    ),
                ),
                (
                    "earea_activity",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        null=True,
                        verbose_name="حوضه فعالیت",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="نام کاربری"
                    ),
                ),
                (
                    "fullname",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="نام کامل"
                    ),
                ),
                ("image", models.ImageField(upload_to="user/user_image")),
                (
                    "date_of_birth",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="تاریخ تولد"
                    ),
                ),
                (
                    "birth_place",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="محل تولد"
                    ),
                ),
                ("instagram", models.CharField(blank=True, max_length=500, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
