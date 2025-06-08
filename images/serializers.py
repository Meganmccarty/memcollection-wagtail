from rest_framework import serializers

from images.models import SpecimenRecordImage, CustomRendition


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


class SpecimenRecordImageSerializer(serializers.ModelSerializer):
    """A serializer for the SpecimenRecordImage model."""

    x_large = RenditionsSerializer()
    large = RenditionsSerializer()
    medium = RenditionsSerializer()
    small = RenditionsSerializer()
    x_small = RenditionsSerializer()
    thumbnail = RenditionsSerializer()

    class Meta:
        model = SpecimenRecordImage
        fields = (
            "id",
            "date_created",
            "date_modified",
            "title",
            "file",
            "description",
            "width",
            "height",
            "created_at",
            "focal_point_x",
            "focal_point_y",
            "focal_point_width",
            "focal_point_height",
            "file_size",
            "file_hash",
            "alt_text",
            "date",
            "notes",
            "position",
            "collection",
            "uploaded_by_user",
            "usi",
            "x_large",
            "large",
            "medium",
            "small",
            "x_small",
            "thumbnail",
        )
