from rest_framework import serializers
from wagtail_footnotes.models import Footnote

from pages.models import SpeciesPage
from taxonomy.serializers import (
    FamilySerializer,
    GenusSerializer,
    OrderSerializer,
    SpeciesSerializer,
    SubfamilySerializer,
    SubspeciesSerializer,
    TribeSerializer,
)


class FootnoteSerializer(serializers.ModelSerializer):
    """A serializer for the Footnote model from wagtail_footnotes."""

    class Meta:
        model = Footnote
        fields = "__all__"


class SpeciesPageSerializer(serializers.ModelSerializer):
    """A serializer for the SpeciesPage model."""

    order = OrderSerializer()
    family = FamilySerializer()
    subfamily = SubfamilySerializer()
    tribe = TribeSerializer()
    genus = GenusSerializer()
    species = SpeciesSerializer()
    subspecies = SubspeciesSerializer(many=True)
    footnotes = FootnoteSerializer(many=True)

    class Meta:
        model = SpeciesPage
        fields = (
            "id",
            "title",
            "slug",
            "order",
            "family",
            "subfamily",
            "tribe",
            "genus",
            "species",
            "subspecies",
            "taxonomy",
            "description",
            "distribution",
            "seasonality",
            "habitat",
            "food",
            "life_cycle",
            "footnotes",
            "first_published_at",
            "last_published_at",
        )
