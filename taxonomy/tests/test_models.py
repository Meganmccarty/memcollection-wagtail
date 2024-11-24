from django.test import TestCase

from taxonomy.models import Order, Species, Subspecies


class TaxonomyBaseTestCase(TestCase):
    """A test case for the TaxonomyBase model.

    This model serves as the base for all of the taxonomy models, so it isn't necessary to test
    each taxonomy model individually. Because TaxonomyBase is an abstract model, the Order model
    will be used in the tests."""

    fixtures = ["orders.json"]

    def test_name(self):
        """Ensures the __str__() method returns the Order object's name."""

        order = Order.objects.get(name="Lepidoptera")
        self.assertEqual(order.__str__(), "Lepidoptera")


class SpeciesTestCase(TestCase):
    """A test case for the Species model.

    The Species model includes some additional fields and methods that are lacking in the
    TaxonomyBase model, so this test case covers those additional aspects."""

    fixtures = [
        "orders.json",
        "families.json",
        "subfamilies.json",
        "tribes.json",
        "genera.json",
        "species.json",
    ]

    def test_name(self):
        """Ensures the __str__() method returns the species' binomial name."""

        species = Species.objects.get(name="polyxenes")
        self.assertEqual(species.__str__(), "Papilio polyxenes")

    def test_binomial(self):
        """Ensures the binomial property returns both the genus and species name."""

        species = Species.objects.get(name="polyxenes")
        self.assertEqual(species.binomial, "Papilio polyxenes")


class SubspeciesTestCase(TestCase):
    """A test case for the Subspecies model.

    The Subspecies model includes some additional fields and methods that are lacking in the
    TaxonomyBase model, so this test case covers those additional aspects."""

    fixtures = [
        "orders.json",
        "families.json",
        "subfamilies.json",
        "tribes.json",
        "genera.json",
        "species.json",
        "subspecies.json",
    ]

    def test_name(self):
        """Ensures the __str__() method returns the subpecies' trinomial name."""

        subspecies = Subspecies.objects.get(name="rudkini")
        self.assertEqual(subspecies.__str__(), "Papilio polyxenes rudkini")

    def test_trinomial(self):
        """Ensures the trinomial property returns the genus, species, and subspecies name."""

        subspecies = Subspecies.objects.get(name="rudkini")
        self.assertEqual(subspecies.trinomial, "Papilio polyxenes rudkini")
