from rest_framework import serializers

from taxonomy.models import Order, Family, Subfamily, Tribe, Genus, Species, Subspecies


class OrderSerializer(serializers.ModelSerializer):
    """A serializer for the Order model.

    It serializes all of the fields on the Order model, including those inherited from the
    TimeStampMixin."""

    class Meta:
        model = Order
        fields = "__all__"


class FamilySerializer(serializers.ModelSerializer):
    """A serializer for the Family model.

    It serializes all of the fields on the Family model, including those inherited from the
    TimeStampMixin. It also serializes the fields from the Order model."""

    order = OrderSerializer()

    class Meta:
        model = Family
        fields = "__all__"


class SubfamilySerializer(serializers.ModelSerializer):
    """A serializer for the Subfamily model.

    It serializes all of the fields from the Subfamily model, including those inherited from the
    TimeStampMixin. It also serializes the fields from the Family and Order models."""

    family = FamilySerializer()

    class Meta:
        model = Subfamily
        fields = "__all__"


class TribeSerializer(serializers.ModelSerializer):
    """A serializer for the Tribe model.

    It serializes all of the fields from the Tribe model, including those inherited from the
    TimeStampMixin. It also serializes the fields from the Subfamily, Family and Order models.
    """

    subfamily = SubfamilySerializer()

    class Meta:
        model = Tribe
        fields = "__all__"


class GenusSerializer(serializers.ModelSerializer):
    """A serializer for the Genus model.

    It serializes all of the fields from the Genus model, including those inherited from the
    TimeStampMixin. It also serializes the fields from the Tribe, Subfamily, Family and Order
    models."""

    tribe = TribeSerializer()

    class Meta:
        model = Genus
        fields = "__all__"


class SpeciesSerializer(serializers.ModelSerializer):
    """A serializer for the Species model.

    It serializes all of the fields from the Species model, including those inherited from the
    TimeStampMixin. It also serializes the fields from the Genus, Tribe, Subfamily, Family and Order
    models."""

    genus = GenusSerializer()

    class Meta:
        model = Species
        fields = "__all__"


class SubspeciesSerializer(serializers.ModelSerializer):
    """A serializer for the Subspecies model.

    It serializes all of the fields from the Genus model, including those inherited from the
    TimeStampMixin. It also serializes the fields from the Species, Genus, Tribe, Subfamily, Family
    and Order models."""

    species = SpeciesSerializer()

    class Meta:
        model = Subspecies
        fields = "__all__"
