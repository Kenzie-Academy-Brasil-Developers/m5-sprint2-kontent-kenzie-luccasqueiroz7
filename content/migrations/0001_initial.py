# Generated by Django 4.1.1 on 2022-09-28 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Content",
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
                ("title", models.CharField(max_length=50)),
                ("module", models.TextField()),
                ("students", models.IntegerField()),
                ("description", models.TextField(null=True)),
                ("is_active", models.BooleanField(default=False)),
            ],
        ),
    ]
