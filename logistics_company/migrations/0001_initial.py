# Generated by Django 5.0.6 on 2024-06-24 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Registry",
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
                ("date", models.DateField(auto_now=True, verbose_name="Дата отгрузки")),
                (
                    "name",
                    models.CharField(
                        max_length=50, verbose_name="Название отправителя"
                    ),
                ),
                ("count", models.IntegerField(verbose_name="Количество мест")),
                ("distance", models.IntegerField(verbose_name="Расстояние")),
            ],
            options={
                "verbose_name": "Реестр",
                "verbose_name_plural": "Реестры",
            },
        ),
    ]
