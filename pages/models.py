from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Page

from taxonomy.models import Species, Subspecies


class SpeciesPage(Page):
    """The model that represents an individual species page.

    Included in this model is the wagtail_footnotes package, so that references can be added to the
    page's content. The ultimate goal would be to structure them on the frontend in a manner similar
    to Wikipedia's footnotes.

    Attributes:
        species (Species): The species that is associated with this page. This is a one to one
                           relationship (a page can have only one species, and a species can have
                           only one page).
        taxonomy (RichTextField): A Wagtail field for adding taxonomy details about a species.
        description (RichTextField): A Wagtail field for adding a description for a species.
        distribution (RichTextField): A Wagtail field for adding information about a species'
                                      distribution.
        seasonality (RichTextField): A Wagtail field for describing a species' seasonality (or
                                     flight periods, in the case of Lepidoptera).
        habitat (RichTextField): A Wagtail field for detailing the habitat of a species
        food (RichTextField): A Wagtail field for listing a species' food sources (both for larval
                              and adult stages).
        life_cycle (RichTextField): A Wagtail field for including details about a species' life
                                    cycle.
    """

    species = models.OneToOneField(
        Species,
        on_delete=models.SET_NULL,
        null=True,
        related_name="species_page",
        help_text="Select the species this page is about",
    )
    taxonomy = RichTextField(default="", blank=True, help_text="Enter taxonomy details")
    description = RichTextField(
        default="", blank=True, help_text="Enter species description"
    )
    distribution = RichTextField(
        default="", blank=True, help_text="Enter distribution details"
    )
    seasonality = RichTextField(
        default="", blank=True, help_text="Enter seasonality details"
    )
    habitat = RichTextField(
        default="", blank=True, help_text="Enter the species' habitat"
    )
    food = RichTextField(
        default="", blank=True, help_text="Enter info larval and adult food sources"
    )
    life_cycle = RichTextField(
        default="", blank=True, help_text="Enter details about the life cycle"
    )

    content_panels = [
        FieldPanel("title"),
        FieldPanel("species"),
        FieldPanel("taxonomy"),
        FieldPanel("description"),
        FieldPanel("distribution"),
        FieldPanel("seasonality"),
        FieldPanel("habitat"),
        FieldPanel("food"),
        FieldPanel("life_cycle"),
        InlinePanel("footnotes", label="Footnotes"),
    ]

    @property
    def subspecies(self):
        """An array of subspecies that belong to this page's species object."""

        return Subspecies.objects.select_related("species").filter(
            species__id=self.species.id
        )
