# Generated by Django 5.1.1 on 2024-09-18 17:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_otp"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="otp",
            name="value",
        ),
        migrations.AddField(
            model_name="otp",
            name="code",
            field=models.CharField(
                db_index=True, default="000000", max_length=6, verbose_name="Code"
            ),
            preserve_default=False,
        ),
    ]
