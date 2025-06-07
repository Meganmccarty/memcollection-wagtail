from wagtail import hooks
from wagtail.admin.panels import FieldPanel, FieldRowPanel, MultiFieldPanel
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet

from specimens.models import Person, SpecimenRecord


@hooks.register("register_icons")
def register_icons(icons):
    return icons + ["specimens/butterfly.svg"]


class PersonSnippet(SnippetViewSet):
    """A snippet for the Person model."""

    model = Person
    menu_icon = "group"
    menu_label = "People"
    menu_name = "people"


class SpecimenRecordSnippet(SnippetViewSet):
    """A snippet for the SpecimenRecord model."""

    model = SpecimenRecord
    menu_icon = "butterfly"
    menu_label = "Specimen Records"
    menu_name = "specimen_records"

    panels = [
        FieldPanel("usi"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("order"),
                        FieldPanel("family"),
                        FieldPanel("subfamily"),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel("tribe"),
                        FieldPanel("genus"),
                        FieldPanel("species"),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel("subspecies"),
                        FieldPanel("determiner"),
                        FieldPanel("determined_year"),
                    ]
                ),
            ],
            heading="Taxonomy Details",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("sex"),
                        FieldPanel("stage"),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel("preparer"),
                        FieldPanel("preparation"),
                        FieldPanel("preparation_date"),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel("labels_printed"),
                        FieldPanel("labeled"),
                        FieldPanel("photographed"),
                    ]
                ),
            ],
            heading="Specimen Details",
        ),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("country"),
                        FieldPanel("state"),
                        FieldPanel("county"),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel("locality"),
                        FieldPanel("gps"),
                        FieldPanel("collecting_trip"),
                    ]
                ),
                FieldRowPanel(
                    [
                        FieldPanel("day"),
                        FieldPanel("month"),
                        FieldPanel("year"),
                    ]
                ),
                FieldPanel("collector"),
                FieldRowPanel(
                    [
                        FieldPanel("method"),
                        FieldPanel("temperature"),
                        FieldPanel("time_of_day"),
                    ]
                ),
                FieldPanel("habitat"),
                FieldPanel("notes"),
            ],
            heading="Locality Details",
        ),
    ]


class SpecimensViewSetGroup(SnippetViewSetGroup):
    """This groups all of the specimen snippets together in the Wagtail admin."""

    items = [
        PersonSnippet,
        SpecimenRecordSnippet,
    ]
    add_to_admin_menu = True
    menu_icon = "butterfly"
    menu_label = "Specimens"
    menu_name = "specimens"


# Registers all of the snippets grouped under the SpecimensViewSetGroup
register_snippet(SpecimensViewSetGroup)
