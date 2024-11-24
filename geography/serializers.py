from rest_framework import serializers

from geography.models import CollectingTrip, Country, County, GPS, Locality, State


class CountrySerializer(serializers.ModelSerializer):
    """A serializer for the Country model.

    It serializes all of the fields on the Country model, including those inherited from the
    TimeStampMixin."""

    class Meta:
        model = Country
        fields = "__all__"


class StateSerializer(serializers.ModelSerializer):
    """A serializer for the State model.

    It serializes all of the fields on the State model, including those inherited from the
    TimeStampMixin. It also serializes the fields from the Country model."""

    country = CountrySerializer()

    class Meta:
        model = State
        fields = "__all__"


class CountySerializer(serializers.ModelSerializer):
    """A serializer for the County model.

    It serializes all of the fields on the County model, including those inherited from the
    TimeStampMixin. It also serializes the fields from the Country and State models."""

    state = StateSerializer()

    class Meta:
        model = County
        fields = "__all__"


class LocalitySerializer(serializers.ModelSerializer):
    """A serializer for the Locality model.

    It serializes all of the fields on the Locality model, including those inherited from the
    TimeStampMixin. It also serializes the fields from the Country, State, and County models.
    """

    country = CountrySerializer()
    state = StateSerializer()
    county = CountySerializer()

    class Meta:
        model = Locality
        fields = "__all__"


class GPSSerializer(serializers.ModelSerializer):
    """A serializer for the GPS model.

    It serializes all of the fields on the GPS model, including those inherited from the
    TimeStampMixin. It also serializes the fields from the Country, State, County, and Locality
    models."""

    locality = LocalitySerializer()

    class Meta:
        model = GPS
        fields = "__all__"


class CollectingTripSerializer(serializers.ModelSerializer):
    """A serializer for the CollectingTrip model.

    It serializes all of the fields on the CollectingTrip model, including those inherited from the
    TimeStampMixin. It also serializes the fields from the Country and State models."""

    states = StateSerializer(many=True)

    class Meta:
        model = CollectingTrip
        fields = "__all__"
