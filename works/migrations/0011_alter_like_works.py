# Generated by Django 4.1.5 on 2023-02-02 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("works", "0010_remove_like_comments_like_works"),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="works",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="likes2",
                to="works.work",
                verbose_name="کار ها",
            ),
        ),
    ]
