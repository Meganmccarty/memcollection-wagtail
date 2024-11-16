from django.test import TestCase

from taxonomy.models import Genus, Order, Species, Subspecies


class TaxonomyBaseTestCase(TestCase):
    """A test case for the TaxonomyBase model.

    This model serves as the base for all of the taxonomy models, so it isn't necessary to test
    each taxonomy model individually. Because TaxonomyBase is an abstract model, the Order model
    will be used in the tests."""

    def setUp(self):
        """Sets up the data needed for testing the Order model."""

        Order.objects.create(
            name="Lepidoptera",
            common_name="Butterflies and Moths",
            authority="Linnaeus, 1758",
        )

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
    ]

    def setUp(self):
        """Sets up the data needed for testing the Species model."""

        Species.objects.create(
            genus=Genus.objects.get(name="Papilio"),
            name="polyxenes",
            common_name="Black Swallowtail",
            authority="Fabricius, 1775",
            mona="4159",
            p3="770301",
        )

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
    ]

    def setUp(self):
        """Sets up the data needed for testing the Subspecies model."""

        Subspecies.objects.create(
            species=Species.objects.get(name="polyxenes"),
            name="coloro",
            common_name="Black Swallowtail",
            authority="(Wright, 1905)",
            mona="4159",
            p3="770301",
        )

    def test_name(self):
        """Ensures the __str__() method returns the subpecies' trinomial name."""

        subspecies = Subspecies.objects.get(name="coloro")
        self.assertEqual(subspecies.__str__(), "Papilio polyxenes coloro")

    def test_trinomial(self):
        """Ensures the trinomial property returns the genus, species, and subspecies name."""

        subspecies = Subspecies.objects.get(name="coloro")
        self.assertEqual(subspecies.trinomial, "Papilio polyxenes coloro")
