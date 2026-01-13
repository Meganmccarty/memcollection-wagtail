from rest_framework import serializers

from geography.serializers import (
    CollectingTripSerializer,
    CountrySerializer,
    CountySerializer,
    GPSSerializer,
    LocalitySerializer,
    StateSerializer,
)
from specimens.models import Person, SpecimenRecord
from taxonomy.serializers import (
    FamilySerializer,
    GenusSerializer,
    OrderSerializer,
    SpeciesSerializer,
    SubfamilySerializer,
    SubspeciesSerializer,
    TribeSerializer,
)


class PersonSerializer(serializers.ModelSerializer):
    """A serializer for the Person model.

    It serializes all of the fields on the Person model, including those inherited from the
    TimeStampMixin."""

    class Meta:
        model = Person
        fields = (
            "id",
            "first_name",
            "middle_initial",
            "last_name",
            "suffix",
            "collector_name",
            "full_name",
            "date_created",
            "date_modified",
        )


class SpecimenRecordSerializer(serializers.ModelSerializer):
    """A serializer for the SpecimenRecord model.

    It serializes all of the fields on the SpecimenRecord model, including those inherited from the
    TimeStampMixin."""

    order = OrderSerializer()
    family = FamilySerializer()
    subfamily = SubfamilySerializer()
    tribe = TribeSerializer()
    genus = GenusSerializer()
    species = SpeciesSerializer()
    subspecies = SubspeciesSerializer()

    determiner = PersonSerializer()
    preparer = PersonSerializer()

    collecting_trip = CollectingTripSerializer()
    country = CountrySerializer()
    state = StateSerializer()
    county = CountySerializer()
    locality = LocalitySerializer()
    gps = GPSSerializer()

    collector = PersonSerializer(many=True)

    taxon = serializers.SerializerMethodField()

    def get_taxon(self, obj):
        """Determine the most specific taxon field."""
        if obj.subspecies:
            return SubspeciesSerializer(obj.subspecies).data
        if obj.species:
            return SpeciesSerializer(obj.species).data
        if obj.genus:
            return GenusSerializer(obj.genus).data
        if obj.tribe:
            return TribeSerializer(obj.tribe).data
        if obj.subfamily:
            return SubfamilySerializer(obj.subfamily).data
        if obj.family:
            return FamilySerializer(obj.family).data
        if obj.order:
            return OrderSerializer(obj.order).data
        return None

    class Meta:
        model = SpecimenRecord
        fields = (
            "id",
            "usi",
            "order",
            "family",
            "subfamily",
            "tribe",
            "genus",
            "species",
            "subspecies",
            "taxon",
            "determiner",
            "determined_year",
            "sex",
            "stage",
            "preparer",
            "preparation",
            "preparation_date",
            "labels_printed",
            "labeled",
            "photographed",
            "identified",
            "collecting_trip",
            "country",
            "state",
            "county",
            "locality",
            "gps",
            "day",
            "month",
            "year",
            "collected_date",
            "full_date",
            "num_date",
            "collector",
            "collectors",
            "method",
            "weather",
            "temperature",
            "temp_F",
            "temp_C",
            "time_of_day",
            "habitat",
            "notes",
            "date_created",
            "date_modified",
        )
