# Generated by Django 4.2.6 on 2023-11-20 20:21

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):
    dependencies = [
        ("password", "0004_alter_password_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="password",
            name="ciphertext",
            field=django_cryptography.fields.encrypt(models.CharField(max_length=1000)),
        ),
    ]
