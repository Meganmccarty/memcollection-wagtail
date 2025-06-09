from rest_framework import serializers

from images.models import CustomImage, CustomRendition, HabitatImage, InsectImage, PlantImage, SpecimenRecordImage


class RenditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomRendition
        fields = (
            "id",
            "date_created",
            "date_modified",
            "filter_spec",
            "file",
            "width",
            "height",
            "focal_point_key",
            "image",
        )


class CustomImageSerializer(serializers.ModelSerializer):
    """A serializer for the CustomImage model."""

    x_large = RenditionsSerializer()
    large = RenditionsSerializer()
    medium = RenditionsSerializer()
    small = RenditionsSerializer()
    x_small = RenditionsSerializer()
    thumbnail = RenditionsSerializer()

    class Meta:
        model = CustomImage
        fields = "__all__"


class SpecimenRecordImageSerializer(CustomImageSerializer):
    """A serializer for the SpecimenRecordImage model."""

    class Meta:
        model = SpecimenRecordImage
        fields = "__all__"


class InsectImageSerializer(CustomImageSerializer):
    """A serializer for the InsectImage model."""

    class Meta:
        model = InsectImage
        fields = "__all__"


class PlantImageSerializer(CustomImageSerializer):
    """A serializer for the PlantImage model."""

    class Meta:
        model = PlantImage
        fields = "__all__"


class HabitatImageSerializer(CustomImageSerializer):
    """A serializer for the HabitatImage model."""

    class Meta:
        model = HabitatImage
        fields = "__all__"


