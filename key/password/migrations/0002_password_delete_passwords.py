# Generated by Django 4.2.6 on 2023-11-04 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("password", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Password",
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
                ("name", models.CharField(max_length=64)),
                ("hash", models.CharField(max_length=1000)),
                ("url", models.CharField(max_length=64)),
                (
                    "tags",
                    models.CharField(
                        choices=[
                            ("blue", "blue"),
                            ("red", "red"),
                            ("green", "green"),
                            ("yellow", "yellow"),
                            ("purple", "purple"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_passwords",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Passwords",
        ),
    ]
