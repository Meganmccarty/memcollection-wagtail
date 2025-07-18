# Generated by Django 5.1.3 on 2024-11-17 02:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxonomy", "0003_subfamily"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tribe",
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
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        help_text="Enter the taxon's scientific name", max_length=100
                    ),
                ),
                (
                    "common_name",
                    models.CharField(
                        blank=True,
                        help_text="Enter the taxon's common name, if it has one",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "authority",
                    models.CharField(
                        help_text="Enter the taxon's authority", max_length=100
                    ),
                ),
                (
                    "subfamily",
                    models.ForeignKey(
                        help_text="Select a subfamily to which this tribe belongs",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="taxonomy.subfamily",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
    ]
