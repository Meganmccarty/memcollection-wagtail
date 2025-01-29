from django.db import models
from wagtail.images.models import AbstractImage, AbstractRendition, Image

from geography.models import CollectingTrip, Country, County, GPS, Locality, State
from mixins.models import TimeStampMixin


class CustomImage(AbstractImage, TimeStampMixin):
    """A custom image model that inherits from both Wagtail's AbstractImage model and my
    TimeStampMixin.

    Attributes:
        alt_text (str): The alternative text of the image.
    """

    alt_text = models.CharField(max_length=255, blank=True)

    admin_form_fields = Image.admin_form_fields + ("alt_text",)


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
