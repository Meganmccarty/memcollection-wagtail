from wagtail.api.v2.views import BaseAPIViewSet

from specimens.models import Person, SpecimenRecord
from specimens.serializers import PersonSerializer, SpecimenRecordSerializer
from utils.helpers import get_fields


class PeopleAPIViewSet(BaseAPIViewSet):
    """A custom API view set for the Person model using the PersonSerializer."""

    base_serializer_class = PersonSerializer
    model = Person
    queryset = Person.objects.all()
    body_fields = get_fields(PersonSerializer)
    listing_default_fields = get_fields(PersonSerializer)


class SpecimenRecordAPIViewSet(BaseAPIViewSet):
    """A custom API view set for the SpecimenRecord model using the
    SpecimenRecordSerializer."""

    base_serializer_class = SpecimenRecordSerializer
    model = SpecimenRecord
    queryset = SpecimenRecord.objects.all()
    body_fields = get_fields(SpecimenRecordSerializer)
    listing_default_fields = get_fields(SpecimenRecordSerializer)
