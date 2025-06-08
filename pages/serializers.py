from rest_framework import serializers
from wagtail_footnotes.models import Footnote

from pages.models import SpeciesPage
from taxonomy.serializers import NestedSpeciesSerializer, SubspeciesSerializer


class FootnoteSerializer(serializers.ModelSerializer):
    """A serializer for the Footnote model from wagtail_footnotes."""

    class Meta:
        model = Footnote
        fields = "__all__"


class SpeciesPageSerializer(serializers.ModelSerializer):
    """A serializer for the SpeciesPage model."""

    species = NestedSpeciesSerializer()
    subspecies = SubspeciesSerializer(many=True)
    footnotes = FootnoteSerializer(many=True)

    class Meta:
        model = SpeciesPage
        fields = (
            "id",
            "species",
            "subspecies",
            "title",
            "slug",
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
