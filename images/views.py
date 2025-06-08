from wagtail.api.v2.views import BaseAPIViewSet

from images.models import SpecimenRecordImage
from images.serializers import SpecimenRecordImageSerializer
from utils.helpers import get_fields


class SpecimenRecordImagesAPIViewSet(BaseAPIViewSet):
    """A custom API view set for the SpecimenRecordImage model using the SpecimenRecordImageSerializer."""

    base_serializer_class = SpecimenRecordImageSerializer
    model = SpecimenRecordImage
    queryset = SpecimenRecordImage.objects.all()
    body_fields = get_fields(SpecimenRecordImageSerializer)
    listing_default_fields = get_fields(SpecimenRecordImageSerializer)
