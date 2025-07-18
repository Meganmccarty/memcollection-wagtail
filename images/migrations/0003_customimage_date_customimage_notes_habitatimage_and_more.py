# Generated by Django 5.1.10 on 2025-06-08 18:14

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0002_remove_customimage_caption_baseliveimage"),
        ("pages", "0002_alter_speciespage_species"),
        ("taxonomy", "0014_alter_subspecies_species"),
    ]

    operations = [
        migrations.AddField(
            model_name="customimage",
            name="date",
            field=models.DateField(
                default="2000-01-01", help_text="Enter the date the image was taken"
            ),
        ),
        migrations.AddField(
            model_name="customimage",
            name="notes",
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.CreateModel(
            name="HabitatImage",
            fields=[
                (
                    "baseliveimage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="images.baseliveimage",
                    ),
                ),
                (
                    "species_page",
                    models.ManyToManyField(
                        help_text="Select the species page(s) to which this habitat image should belong",
                        related_name="habitat_images",
                        to="pages.speciespage",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("images.baseliveimage",),
        ),
        migrations.CreateModel(
            name="InsectImage",
            fields=[
                (
                    "baseliveimage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="images.baseliveimage",
                    ),
                ),
                (
                    "sex",
                    models.CharField(
                        choices=[
                            ("male", "male"),
                            ("female", "female"),
                            ("unknown", "unknown"),
                        ],
                        default="unknown",
                        help_text="Select the insect's sex",
                        max_length=10,
                    ),
                ),
                (
                    "stage",
                    models.CharField(
                        choices=[
                            ("egg", "egg"),
                            ("larva", "larva"),
                            ("nymph", "nymph"),
                            ("pupa", "pupa"),
                            ("adult", "adult"),
                        ],
                        default="adult",
                        help_text="Select the insect's stage",
                        max_length=10,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("wild", "wild"),
                            ("reared", "reared"),
                            ("bred", "bred"),
                        ],
                        default="wild",
                        help_text="Select the status of the insect in the image",
                        max_length=10,
                    ),
                ),
                (
                    "species",
                    models.ForeignKey(
                        blank=True,
                        help_text="Select the species in the image, if it is identified",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="insect_images",
                        to="taxonomy.species",
                    ),
                ),
                (
                    "species_page",
                    models.ForeignKey(
                        blank=True,
                        help_text="Select the species page to which this image belongs, if the insect in the image is identified",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="insect_images",
                        to="pages.speciespage",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("images.baseliveimage",),
        ),
        migrations.CreateModel(
            name="PlantImage",
            fields=[
                (
                    "baseliveimage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="images.baseliveimage",
                    ),
                ),
                (
                    "scientific_name",
                    models.CharField(
                        blank=True,
                        help_text="Enter the scientific name of the plant, if known",
                        max_length=100,
                    ),
                ),
                (
                    "common_name",
                    models.CharField(
                        blank=True,
                        help_text="Enter the common name of the plant, if known",
                        max_length=100,
                    ),
                ),
                (
                    "species_page",
                    models.ManyToManyField(
                        help_text="Select the species pages(s) to which this plant image should belong",
                        related_name="plant_images",
                        to="pages.speciespage",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("images.baseliveimage",),
        ),
    ]
