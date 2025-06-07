from django.db import models
from django.template.defaultfilters import slugify
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Page

from taxonomy.models import Species

class SpeciesPage(Page):
    """The model that represents an individual species page."""

    species = models.OneToOneField(
        Species,
        on_delete=models.SET_NULL,
        null=True,
        related_name="species_page",
        help_text="Select the species this page is about",
    )
    taxonomy = RichTextField(default='', blank=True, help_text='Enter taxonomy details')
    description = RichTextField(default='', blank=True, help_text='Enter species description')
    distribution = RichTextField(default='', blank=True, help_text='Enter distribution details')
    seasonality = RichTextField(default='', blank=True, help_text='Enter seasonality details')
    habitat = RichTextField(default='', blank=True, help_text='Enter the species\' habitat')
    food = RichTextField(default='', blank=True, help_text='Enter info larval and adult food sources')
    life_cycle = RichTextField(default='', blank=True, help_text='Enter details about the life cycle')

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
