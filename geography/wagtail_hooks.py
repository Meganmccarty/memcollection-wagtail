from wagtail.admin.panels import FieldPanel, HelpPanel, MultiFieldPanel
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet

from geography.models import CollectingTrip, Country, County, GPS, Locality, State


class CountrySnippet(SnippetViewSet):
    """A snippet for the Country model."""

    model = Country
    menu_icon = "globe"
    menu_label = "Countries"
    menu_name = "countries"


class StateSnippet(SnippetViewSet):
    """A snippet for the State model."""

    model = State
    menu_icon = "globe"
    menu_label = "States"
    menu_name = "states"


class CountySnippet(SnippetViewSet):
    """A snippet for the County model."""

    model = County
    menu_icon = "globe"
    menu_label = "Counties"
    menu_name = "counties"


class LocalitySnippet(SnippetViewSet):
    """A snippet for the Locality model.

    It includes some custom panels for display in the Wagtail admin. While these panels could be
    included directly within the Locality model, I chose to separate as much of the Wagtail logic
    as possible from the plain Django model."""

    model = Locality
    menu_icon = "globe"
    menu_label = "Localities"
    menu_name = "localities"

    panels = [
        FieldPanel("name"),
        FieldPanel("range"),
        FieldPanel("town"),
        MultiFieldPanel(
            [
                HelpPanel(
                    heading="Note:", content="Choose a maximum of 1 option below)"
                ),
                FieldPanel("county"),
                FieldPanel("state"),
                FieldPanel("country"),
            ]
        ),
    ]


class GPSSnippet(SnippetViewSet):
    """A snippet for the GPS model."""

    model = GPS
    menu_icon = "globe"
    menu_label = "GPS Coordinates"
    menu_name = "gps_coordinates"


class CollectingTripSnippet(SnippetViewSet):
    """A snippet for the CollectingTrip model."""

    model = CollectingTrip
    menu_icon = "globe"
    menu_label = "Collecting Trips"
    menu_name = "collecting_trips"


class GeographyViewSetGroup(SnippetViewSetGroup):
    """This groups all of the geography snippets together in the Wagtail admin."""

    items = (
        CountrySnippet,
        StateSnippet,
        CountySnippet,
        LocalitySnippet,
        GPSSnippet,
        CollectingTripSnippet,
    )
    add_to_admin_menu = True
    menu_icon = "site"
    menu_label = "Geography"
    menu_name = "geography"


# Registers all of the snippets grouped under the GeographyViewSetGroup
register_snippet(GeographyViewSetGroup)
