from wagtail.api.v2.views import BaseAPIViewSet

from pages.models import SpeciesPage
from pages.serializers import SpeciesPageSerializer
from utils.helpers import get_fields


class SpeciesPagesAPIViewSet(BaseAPIViewSet):
    """A custom API view set for the SpeciesPage model using the SpeciesPageSerializer."""

    base_serializer_class = SpeciesPageSerializer
    model = SpeciesPage
    queryset = SpeciesPage.objects.all()
    body_fields = get_fields(SpeciesPageSerializer)
    listing_default_fields = get_fields(SpeciesPageSerializer)
