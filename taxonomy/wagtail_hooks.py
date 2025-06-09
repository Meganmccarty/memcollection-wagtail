from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet

from taxonomy.models import Family, Genus, Order, Species, Subfamily, Subspecies, Tribe


class OrderSnippet(SnippetViewSet):
    """A snippet for the Order model."""

    model = Order
    menu_icon = "list-ul"
    menu_label = "Orders"
    menu_name = "orders"


class FamilySnippet(SnippetViewSet):
    """A snippet for the family model."""

    model = Family
    menu_icon = "list-ul"
    menu_label = "Families"
    menu_name = "families"


class SubfamilySnippet(SnippetViewSet):
    """A snippet for the subfamily model."""

    model = Subfamily
    menu_icon = "list-ul"
    menu_label = "Subfamilies"
    menu_name = "subfamilies"


class TribeSnippet(SnippetViewSet):
    """A snippet for the tribe model."""

    model = Tribe
    menu_icon = "list-ul"
    menu_label = "Tribes"
    menu_name = "tribes"


class GenusSnippet(SnippetViewSet):
    """A snippet for the genus model."""

    model = Genus
    menu_icon = "list-ul"
    menu_label = "Genera"
    menu_name = "genera"


class SpeciesSnippet(SnippetViewSet):
    """A snippet for the species model."""

    model = Species
    menu_icon = "list-ul"
    menu_label = "Species"
    menu_name = "species"


class SubspeciesSnippet(SnippetViewSet):
    """A snippet for the subspecies model."""

    model = Subspecies
    menu_icon = "list-ul"
    menu_label = "Subspecies"
    menu_name = "subspecies"


class TaxonomyViewSetGroup(SnippetViewSetGroup):
    """This groups all of the taxonomy snippets together in the Wagtail admin."""

    items = [
        OrderSnippet,
        FamilySnippet,
        SubfamilySnippet,
        TribeSnippet,
        GenusSnippet,
        SpeciesSnippet,
        SubspeciesSnippet,
    ]
    add_to_admin_menu = True
    menu_icon = "form"
    menu_label = "Taxonomy"
    menu_name = "taxonomy"
    menu_order = 70


# Registers all of the snippets grouped under the TaxonomyViewSetGroup
register_snippet(TaxonomyViewSetGroup)
