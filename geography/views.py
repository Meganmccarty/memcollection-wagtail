from wagtail.api.v2.views import BaseAPIViewSet

from geography.models import CollectingTrip, County, Country, GPS, Locality, State
from geography.serializers import (
    CollectingTripSerializer,
    CountySerializer,
    CountrySerializer,
    GPSSerializer,
    LocalitySerializer,
    StateSerializer,
)


class CountriesAPIViewSet(BaseAPIViewSet):
    """A custom API view set for the Country model using the CountrySerializer."""

    base_serializer_class = CountrySerializer
    model = Country


class StatesAPIViewSet(BaseAPIViewSet):
    """A custom API view set for the State model using the StateSerializer."""

    base_serializer_class = StateSerializer
    model = State


class CountiesAPIViewSet(BaseAPIViewSet):
    """A custom API view set for the County model using the CountySerializer."""

    base_serializer_class = CountySerializer
    model = County


class LocalitiesAPIViewSet(BaseAPIViewSet):
    """A custom API view set for the Locality model using the LocalitySerializer."""

    base_serializer_class = LocalitySerializer
    model = Locality


class GPSAPIViewSet(BaseAPIViewSet):
    """A custom API view set for the GPS model using the GPSSerializer."""

    base_serializer_class = GPSSerializer
    model = GPS


class CollectingTripsAPIViewSet(BaseAPIViewSet):
    """A custom API view set for the CollectingTrip model using the CollectingTripSerializer."""

    base_serializer_class = CollectingTripSerializer
    model = CollectingTrip
