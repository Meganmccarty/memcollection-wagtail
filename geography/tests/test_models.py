from django.core.exceptions import ValidationError
from django.test import TestCase

from geography.models import CollectingTrip, County, Country, GPS, Locality, State


class CountryTestCase(TestCase):
    """A test case for the Country model."""

    fixtures = ["countries.json"]

    def test_name(self):
        """Ensures the __str__() method returns the country's name."""

        country = Country.objects.get(name="United States of America")
        self.assertEqual(country.__str__(), "United States of America")


class StateTestCase(TestCase):
    """A test case for the State model."""

    fixtures = ["countries.json", "states.json"]

    def test_name(self):
        """Ensures the __str__() method returns the state's name."""

        state = State.objects.get(name="Indiana")
        self.assertEqual(state.__str__(), "Indiana")


class CountyTestCase(TestCase):
    """A test case for the County model."""

    fixtures = ["countries.json", "states.json", "counties.json"]

    def test_name(self):
        """Ensures the __str__() method returns the county's name, abbr, and state abbr.

        In some cases, a county will not have an abbreviation (like a census area in Alaska). This
        test covers that edge case."""

        county = County.objects.get(name="Switzerland")
        parish = County.objects.get(name="Rapides")
        borough = County.objects.get(name="Fairbanks N. Star")
        census_area = County.objects.get(name="Yukon-Koyukuk Census Area")
        county_line = County.objects.get(name="Clear Creek/Summit")

        self.assertEqual(county.__str__(), "Switzerland Co., IN")
        self.assertEqual(parish.__str__(), "Rapides Par., LA")
        self.assertEqual(borough.__str__(), "Fairbanks N. Star Boro., AK")
        self.assertEqual(census_area.__str__(), "Yukon-Koyukuk Census Area, AK")
        self.assertEqual(county_line.__str__(), "Clear Creek/Summit Co. line, CO")

    def test_abbr(self):
        """Ensures the correct county abbreviation is created based on what state the county is in.

        Most states in the US are broken up into smaller units called counties, but some states
        call their smaller divisions parishes (Louisiana) or boroughs (Alaska). Alaska also has
        census areas, which do not have an abbreviation."""

        county = County.objects.get(name="Switzerland")
        parish = County.objects.get(name="Rapides")
        borough = County.objects.get(name="Fairbanks N. Star")
        census_area = County.objects.get(name="Yukon-Koyukuk Census Area")

        self.assertEqual(county.abbr, "Co.")
        self.assertEqual(parish.abbr, "Par.")
        self.assertEqual(borough.abbr, "Boro.")
        self.assertEqual(census_area.abbr, "")

    def test_county_line(self):
        """Ensures a county has a property containing either "line" or "".

        There are cases where a County object instance will have two counties listed in the name
        instead of one. This is due to cases where a specimen has been collected on the border
        between two counties (on the county line)."""

        county_no_line = County.objects.get(name="Switzerland")
        county_line = County.objects.get(name="Clear Creek/Summit")

        self.assertEqual(county_no_line.county_line, "")
        self.assertEqual(county_line.county_line, "line")

    def test_full_name(self):
        """Ensures a county has a property containing its name, abbreviation, and line."""

        census_area = County.objects.get(name="Yukon-Koyukuk Census Area")
        county_line = County.objects.get(name="Clear Creek/Summit")

        self.assertEqual(census_area.full_name, "Yukon-Koyukuk Census Area")
        self.assertEqual(county_line.full_name, "Clear Creek/Summit Co. line")


class LocalityTestCase(TestCase):
    """A test case for the Locality model."""

    fixtures = ["countries.json", "states.json", "counties.json", "localities.json"]

    def test_name(self):
        """Ensures the __str__() method returns the correct info for a given locality."""

        locality_county_all = Locality.objects.get(
            name="Bonanza Creek Experimental Forest"
        )
        locality_county_no_name = Locality.objects.get(
            range="4 km NW", town="Patriot", name=None
        )
        locality_county_no_range = Locality.objects.get(
            name="Big Oaks NWR", town="Madison"
        )
        locality_state_no_name_range = Locality.objects.get(town="Montague")
        locality_country_no_range_town = Locality.objects.get(
            name="Carolina Biological Supply Company"
        )
        locality_country_no_name_range = Locality.objects.get(town="Mexico City")

        self.assertEqual(
            locality_county_all.__str__(),
            "Bonanza Creek Experimental Forest, 23 km SW Ester, Fairbanks N. Star Boro.",
        )
        self.assertEqual(
            locality_county_no_name.__str__(), "4 km NW Patriot, Switzerland Co."
        )
        self.assertEqual(
            locality_county_no_range.__str__(), "Big Oaks NWR, Madison, Jefferson Co."
        )
        self.assertEqual(locality_state_no_name_range.__str__(), "Montague, PEI")
        self.assertEqual(
            locality_country_no_range_town.__str__(),
            "Carolina Biological Supply Company, USA",
        )
        self.assertEqual(locality_country_no_name_range.__str__(), "Mexico City, MEX")

    def test_clean(self):
        """Ensures the clean() method validates the use of the county, state, and country fields.

        A Locality object instance can have only one county, state, or country field NOT be null.
        """

        # County and State NOT NULL
        locality_with_county_state = Locality.objects.create(
            name="Test National Forest",
            county=County.objects.get(name="Switzerland"),
            state=State.objects.get(name="Indiana"),
        )
        errors_with_county_state = {
            "county": ["You cannot select both a county and a state"],
            "state": ["You cannot select both a county and a state"],
        }
        self.assertRaises(
            ValidationError, locality_with_county_state.full_clean
        ), errors_with_county_state

        # County and Country NOT NULL
        locality_with_county_country = Locality.objects.create(
            name="Test National Forest",
            county=County.objects.get(name="Rapides"),
            country=Country.objects.get(name="United States of America"),
        )
        errors_with_county_country = {
            "county": ["You cannot select both a county and a country"],
            "country": ["You cannot select both a county and a country"],
        }
        self.assertRaises(
            ValidationError, locality_with_county_country.full_clean
        ), errors_with_county_country

        # State and Country NOT NULL
        locality_with_state_country = Locality.objects.create(
            name="Test National Forest",
            state=State.objects.get(name="Wyoming"),
            country=Country.objects.get(name="United States of America"),
        )
        errors_with_state_country = {
            "state": ["You cannot select both a state and a country"],
            "country": ["You cannot select both a state and a country"],
        }
        self.assertRaises(
            ValidationError, locality_with_state_country.full_clean
        ), errors_with_state_country

        # County, State, and Country NOT NULL
        locality_with_three_regions = Locality.objects.create(
            name="Test National Forest",
            county=County.objects.get(name="Fairbanks N. Star"),
            state=State.objects.get(name="Alaska"),
            country=Country.objects.get(name="United States of America"),
        )
        errors_with_three_regions = {
            "county": ["You cannot select a county, state, and country together"],
            "state": ["You cannot select a county, state, and country together"],
            "country": ["You cannot select a county, state, and country together"],
        }
        self.assertRaises(
            ValidationError,
            locality_with_three_regions.full_clean,
            errors_with_three_regions,
        )


class GPSTestCase(TestCase):
    """A test case for the GPS model."""

    fixtures = [
        "countries.json",
        "states.json",
        "counties.json",
        "localities.json",
        "gps_coordinates.json",
    ]

    def test_name(self):
        """Ensures the __str__() method returns the correct info for a given GPS object instance."""

        gps_coordinates = GPS.objects.get(latitude="38.849500")
        no_gps_coordinates = GPS.objects.get(elevation="3157-3402")

        self.assertEqual(
            gps_coordinates.__str__(),
            "38.849500 -84.866328 252m, Boone Robinson Rd, 4 km NW Patriot, Switzerland Co.",
        )
        self.assertEqual(
            no_gps_coordinates.__str__(),
            "3157-3402m, William's Lake Trail, Carson NF, Taos Ski Valley, Taos Co.",
        )

    def test_elevation_meters(self):
        """Ensures an "m" is appended to the elevation."""

        no_gps_coordinates = GPS.objects.get(elevation="3157-3402")
        self.assertEqual(no_gps_coordinates.elevation_meters, "3157-3402m")


class CollectingTripTestCase(TestCase):
    """A test case for the CollectingTrip model."""

    fixtures = ["countries.json", "states.json", "collecting_trips.json"]

    def test_name(self):
        """Ensures the __str__() method returns the correct info for a CollectingTrip."""

        trip = CollectingTrip.objects.get(name="LepSoc 2008")
        self.assertEqual(trip.__str__(), "LepSoc 2008")

    def test_slug(self):
        """Ensures the slug() method returns properly slugifies a CollectingTrip's name."""

        trip = CollectingTrip.objects.get(name="LepSoc 2008")
        self.assertEqual(trip.slug, "lepsoc-2008")
