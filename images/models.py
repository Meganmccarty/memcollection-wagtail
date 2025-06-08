from django.db import models
from wagtail.fields import RichTextField
from wagtail.images.models import AbstractImage, AbstractRendition, Image

from geography.models import CollectingTrip, Country, County, GPS, Locality, State
from mixins.models import TimeStampMixin
from pages.models import SpeciesPage
from specimens.models import SpecimenRecord
from taxonomy.models import Species
from utils.insect_attributes import Sex, Stage


class CustomImage(AbstractImage, TimeStampMixin):
    """A custom image model that inherits from both Wagtail's AbstractImage model and my
    TimeStampMixin.

    Attributes:
        alt_text (str): The alternative text of the image.
    """

    alt_text = models.CharField(max_length=255, blank=True)
    date = models.DateField(help_text="Enter the date the image was taken")
    notes = RichTextField(blank=True)

    admin_form_fields = Image.admin_form_fields + ("alt_text", "date", "notes")

    @property
    def x_large(self):
        return self.get_rendition("max-2000x2000")

    @property
    def large(self):
        return self.get_rendition("max-1500x1500")

    @property
    def medium(self):
        return self.get_rendition("max-1200x1200")

    @property
    def small(self):
        return self.get_rendition("max-900x900")

    @property
    def x_small(self):
        return self.get_rendition("max-600x600")

    @property
    def thumbnail(self):
        return self.get_rendition("max-300x300")


class CustomRendition(AbstractRendition, TimeStampMixin):
    """A customm rendition model that inherits from both Wagtail's AbstractRendition model and my
    TimeStampMixin.

    Attributes:
        image (CustomImage): The image to which this rendition belongs.
    """

    image = models.ForeignKey(
        CustomImage, on_delete=models.CASCADE, related_name="renditions"
    )

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)


class BaseLiveImage(CustomImage):
    """An image model containing fields used for all types of live images (whether insects, plants,
    or habitats).

    Attributes:
        country (Country): The country in which the image was taken.
        state (State): The state (or province) in which the image was taken.
        county (County): The county (or parish or census area) in which the image was taken.
        locality (Locality): The locality at which the image was taken.
        gps (GPS): The GPS coordinates at which the image was taken.
        collecting_trip (CollectingTrip): The collecting trip during which the image was taken.
    """

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="%(class)s",
        null=True,
        blank=True,
        help_text="Select the country in which the image was taken",
    )
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name="%(class)s",
        null=True,
        blank=True,
        help_text="Select the state in which the image was taken",
    )
    county = models.ForeignKey(
        County,
        on_delete=models.CASCADE,
        related_name="%(class)s",
        null=True,
        blank=True,
        help_text="Select the county in which the image was taken",
    )
    locality = models.ForeignKey(
        Locality,
        on_delete=models.CASCADE,
        related_name="%(class)s",
        null=True,
        blank=True,
        help_text="Select the locality at which the image was taken",
    )
    gps = models.ForeignKey(
        GPS,
        on_delete=models.CASCADE,
        related_name="%(class)s",
        null=True,
        blank=True,
        help_text="Select the GPS coordinates at which the image was taken",
    )
    collecting_trip = models.ForeignKey(
        CollectingTrip,
        on_delete=models.CASCADE,
        related_name="%(class)s",
        null=True,
        blank=True,
        help_text="Select the collecting trip during which the image was taken",
    )


class SpecimenRecordImage(CustomImage):
    usi = models.ForeignKey(SpecimenRecord, on_delete=models.CASCADE,
        related_name='specimen_images', help_text='Select the specimen in the image')

    class Position(models.TextChoices):
        DORSAL = "dorsal", "dorsal"
        VENTRAL = "ventral", "ventral"
        LATERAL = "lateral", "lateral"

    position = models.CharField(max_length=10, choices=Position.choices, default=Position.DORSAL,
        help_text='Select the view of the specimen in the image')



class InsectImage(BaseLiveImage):
    """An image model for a live insect image."""

    species = models.ForeignKey(Species, on_delete=models.CASCADE, null=True, blank=True, related_name="insect_images", help_text="Select the species in the image, if it is identified")
    species_page = models.ForeignKey(SpeciesPage, on_delete=models.CASCADE, null=True, blank=True, related_name="insect_images", help_text="Select the species page to which this image belongs, if the insect in the image is identified")
    featured_family = models.BooleanField(default=False, help_text="Toggle to make this image represent the family to which the insect in the image belongs")
    featured_species = models.BooleanField(default=False, help_text="Toggle to make this image represent the species to which the insect in the image belongs")

    class Status(models.TextChoices):
        WILD = "wild", "wild"
        REARED = "reared", "reared"
        BRED = "bred", "bred"

    sex = models.CharField(
        max_length=10,
        choices=Sex.choices,
        default=Sex.UNKNOWN,
        help_text="Select the insect's sex",
    )
    stage = models.CharField(
        max_length=10,
        choices=Stage.choices,
        default=Stage.ADULT,
        help_text="Select the insect's stage",
    )
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.WILD,
        help_text="Select the status of the insect in the image")

    @property
    def identified(self):
        if self.species and self.species_page:
            return True
        else:
            return False
    
    @property
    def family(self):
        if self.featured_family == True:
            return self.species.genus.tribe.subfamily.family.name
        else:
            return ""
        
    @property
    def species_binomial(self):
        if self.featured_species == True:
            return self.species.binomial
        else:
            return ""


class PlantImage(BaseLiveImage):
    species_page = models.ManyToManyField(SpeciesPage, related_name='plant_images',
        help_text='Select the species pages(s) to which this plant image should belong')
    scientific_name = models.CharField(max_length=100, blank=True,
        help_text='Enter the scientific name of the plant, if known')
    common_name = models.CharField(max_length=100, blank=True,
        help_text='Enter the common name of the plant, if known')


class HabitatImage(BaseLiveImage):
    species_page = models.ManyToManyField(SpeciesPage, related_name='habitat_images',
        help_text='Select the species page(s) to which this habitat image should belong')
