from rest_framework import serializers

from geography.models import CollectingTrip, Country, County, GPS, Locality, State


class CountrySerializer(serializers.ModelSerializer):
    """A serializer for the Country model.

    It serializes all of the fields on the Country model, including those inherited from the
    TimeStampMixin."""

    class Meta:
        model = Country
        fields = ("id", "name", "abbr", "date_created", "date_modified")


class StateSerializer(serializers.ModelSerializer):
    """A serializer for the State model.

    It serializes all of the fields on the State model, including those inherited from the
    TimeStampMixin."""

    class Meta:
        model = State
        fields = ("id", "name", "abbr", "date_created", "date_modified", "country")


class CountySerializer(serializers.ModelSerializer):
    """A serializer for the County model.

    It serializes all of the fields on the County model, including those inherited from the
    TimeStampMixin."""

    full_name = serializers.CharField()

    class Meta:
        model = County
        fields = (
            "id",
            "name",
            "abbr",
            "full_name",
            "date_created",
            "date_modified",
            "state",
        )


class LocalitySerializer(serializers.ModelSerializer):
    """A serializer for the Locality model.

    It serializes all of the fields on the Locality model, including those inherited from the
    TimeStampMixin."""

    class Meta:
        model = Locality
        fields = (
            "id",
            "name",
            "range",
            "town",
            "date_created",
            "date_modified",
            "country",
            "state",
            "county",
        )


class GPSSerializer(serializers.ModelSerializer):
    """A serializer for the GPS model.

    It serializes all of the fields on the GPS model, including those inherited from the
    TimeStampMixin. It also serializes the fields from the Country, State, County, and Locality
    models."""

    elevation_meters = serializers.CharField()

    class Meta:
        model = GPS
        fields = (
            "id",
            "latitude",
            "longitude",
            "elevation",
            "elevation_meters",
            "date_created",
            "date_modified",
            "locality",
        )


class CollectingTripSerializer(serializers.ModelSerializer):
    """A serializer for the CollectingTrip model.

    It serializes all of the fields on the CollectingTrip model, including those inherited from the
    TimeStampMixin. It also serializes the fields from and State model."""

    states = StateSerializer(many=True)

    class Meta:
        model = CollectingTrip
        fields = (
            "id",
            "name",
            "slug",
            "states",
            "start_date",
            "end_date",
            "notes",
            "date_created",
            "date_modified",
        )


class NestedStateSerializer(StateSerializer):
    """A serializer for the State model that includes nested data.

    It extends the StateSerializer and includes all of the data wthin the country field using the
    CountrySerializer."""

    country = CountrySerializer()


class NestedCountySerializer(CountySerializer):
    """A serializer for the County model that includes nested data.

    It extends the CountySerializer and includes all of the data within the state field using the
    NestedStateSerializer."""

    state = NestedStateSerializer()


class NestedLocalitySerializer(LocalitySerializer):
    """A serializer for the Locality model that includes nested data.

    It extends the LocalitySerializer and includes all of the data within the country, state, and
    county fields using their respective serializers."""

    country = CountrySerializer()
    state = StateSerializer()
    county = CountySerializer()


class NestedGPSSerializer(GPSSerializer):
    """A serializer for the GPS model that includes nested data.

    It extends the GPSSerializer and includes all of the data within the locality field using the
    NestedLocalitySerializer."""

    locality = NestedLocalitySerializer()
