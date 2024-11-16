from django.test import TestCase
from rest_framework.test import APIRequestFactory

from geography.models import CollectingTrip, County, Country, GPS, Locality, State
from geography.serializers import (
    CollectingTripSerializer,
    CountySerializer,
    CountrySerializer,
    GPSSerializer,
    LocalitySerializer,
    StateSerializer,
)


class CountrySerializerTestCase(TestCase):
    """A test case for the CountrySerializer."""

    def setUp(self):
        """Sets up the data needed for testing the CountrySerializer."""

        Country.objects.create(name="United States of America", abbr="USA")

    def test_serializer(self):
        """Ensures the country data is properly serialized."""
        country = Country.objects.get(name="United States of America")

        factory = APIRequestFactory()
        request = factory.post("/api/v2/countries/", {})
        data = CountrySerializer(country, context={"request": request}).data

        self.assertEqual(data["name"], "United States of America")
        self.assertEqual(data["abbr"], "USA")


class StateSerializerTestCase(TestCase):
    """A test case for the StateSerializer."""

    fixtures = ["countries.json"]

    def setUp(self):
        """Sets up the data needed for testing the StateSerializer."""

        State.objects.create(
            name="Indiana", abbr="IN", country=Country.objects.get(abbr="USA")
        )

    def test_serializer(self):
        """Ensures the state data is properly serialized."""
        country = State.objects.get(name="Indiana")

        factory = APIRequestFactory()
        request = factory.post("/api/v2/states/", {})
        data = StateSerializer(country, context={"request": request}).data

        self.assertEqual(data["name"], "Indiana")
        self.assertEqual(data["abbr"], "IN")


class CountySerializerTestCase(TestCase):
    """A test case for the CountySerializer."""

    fixtures = ["countries.json", "states.json"]

    def setUp(self):
        """Sets up the data needed for testing the CountySerializer."""

        County.objects.create(
            name="Switzerland", state=State.objects.get(name="Indiana")
        )

    def test_serializer(self):
        """Ensures the county data is properly serialized."""
        county = County.objects.get(name="Switzerland")

        factory = APIRequestFactory()
        request = factory.post("/api/v2/counties/", {})
        data = CountySerializer(county, context={"request": request}).data

        self.assertEqual(data["name"], "Switzerland")
        self.assertEqual(data["abbr"], "Co.")
        self.assertEqual(data["full_name"], "Switzerland Co.")
        self.assertEqual(data["country"]["name"], "United States of America")
        self.assertEqual(data["country"]["abbr"], "USA")
        self.assertEqual(data["state"]["name"], "Indiana")
        self.assertEqual(data["state"]["abbr"], "IN")


class LocalitySerializerTestCase(TestCase):
    """A test case for the LocalitySerializer."""

    fixtures = ["countries.json", "states.json", "counties.json"]

    def setUp(self):
        """Sets up the data needed for testing the LocalitySerializer."""

        Locality.objects.create(
            name="Bonanza Creek Experimental Forest",
            range="23 km SW",
            town="Ester",
            county=County.objects.get(name="Fairbanks N. Star"),
        )
        Locality.objects.create(
            town="Montague", state=State.objects.get(name="Prince Edward Island")
        )
        Locality.objects.create(
            town="Mexico City", country=Country.objects.get(name="Mexico")
        )

    def test_serializer(self):
        """Ensures the locality data is properly serialized."""

        locality_fields_all = Locality.objects.get(
            name="Bonanza Creek Experimental Forest"
        )
        locality_with_state = Locality.objects.get(town="Montague")
        locality_with_country = Locality.objects.get(town="Mexico City")

        factory = APIRequestFactory()
        request = factory.post("/api/v2/localities/", {})
        data_fields_all = LocalitySerializer(
            locality_fields_all, context={"request": request}
        ).data
        data_with_state = LocalitySerializer(
            locality_with_state, context={"request": request}
        ).data
        data_with_country = LocalitySerializer(
            locality_with_country, context={"request": request}
        ).data

        self.assertEqual(data_fields_all["name"], "Bonanza Creek Experimental Forest")
        self.assertEqual(data_fields_all["range"], "23 km SW")
        self.assertEqual(data_fields_all["town"], "Ester")
        self.assertEqual(data_fields_all["county"]["name"], "Fairbanks N. Star")
        self.assertEqual(data_fields_all["county"]["abbr"], "Boro.")

        self.assertEqual(data_with_state["state"]["name"], "Prince Edward Island")
        self.assertEqual(data_with_country["country"]["name"], "Mexico")


class GPSSerializerTestCase(TestCase):
    """A test case for the GPSSerializer."""

    fixtures = ["countries.json", "states.json", "counties.json", "localities.json"]

    def setUp(self):
        """Sets up the data needed for testing the GPSSerializer."""

        GPS.objects.create(
            locality=Locality.objects.get(name="Boone Robinson Rd"),
            latitude=38.849500,
            longitude=-84.866328,
            elevation="252",
        )
        GPS.objects.create(
            locality=Locality.objects.get(name="William's Lake Trail, Carson NF"),
            elevation="3157-3402",
        )

    def test_serializer(self):
        """Ensures the GPS data is properly serialized."""

        gps_coordinates = GPS.objects.get(latitude=38.849500)
        no_gps_coordinates = GPS.objects.get(elevation="3157-3402")

        factory = APIRequestFactory()
        request = factory.post("/api/v2/gps-coordinates/", {})
        data_gps_coordinates = GPSSerializer(
            gps_coordinates, context={"request": request}
        ).data
        data_no_gps_coordinates = GPSSerializer(
            no_gps_coordinates, context={"request": request}
        ).data

        self.assertEqual(data_gps_coordinates["latitude"], "38.849500")
        self.assertEqual(data_gps_coordinates["longitude"], "-84.866328")
        self.assertEqual(data_gps_coordinates["elevation"], "252")
        self.assertEqual(data_gps_coordinates["elevation_meters"], "252m")
        self.assertEqual(data_gps_coordinates["locality"]["name"], "Boone Robinson Rd")
        self.assertEqual(data_gps_coordinates["locality"]["range"], "4 km NW")
        self.assertEqual(data_gps_coordinates["locality"]["town"], "Patriot")
        self.assertEqual(data_no_gps_coordinates["elevation"], "3157-3402")
        self.assertEqual(data_no_gps_coordinates["elevation_meters"], "3157-3402m")


class CollectingTripSerializerTestCase(TestCase):
    """A test case for the CollectingTripSerializer."""

    fixtures = ["countries.json", "states.json"]

    def setUp(self):
        """Sets up the data needed for testing the CollectingTripSerializer."""

        trip = CollectingTrip.objects.create(
            name="LepSoc 2008", start_date="2008-06-24", end_date="2008-06-28"
        )
        ms = State.objects.get(name="Mississippi")
        tn = State.objects.get(name="Tennessee")
        trip.states.add(ms.id, tn.id)

    def test_serializer(self):
        """Ensures the CollectingTrip data is properly serialized."""

        trip = CollectingTrip.objects.get(name="LepSoc 2008")

        factory = APIRequestFactory()
        request = factory.post("/api/v2/collecting-trips/", {})
        data = CollectingTripSerializer(trip, context={"request": request}).data

        self.assertEqual(data["name"], "LepSoc 2008")
        self.assertEqual(data["start_date"], "2008-06-24")
        self.assertEqual(data["end_date"], "2008-06-28")
        self.assertEqual(data["slug"], "lepsoc-2008")
        self.assertEqual(data["states"][0]["name"], "Mississippi")
        self.assertEqual(data["states"][1]["name"], "Tennessee")
