from wagtail.api.v2.views import BaseAPIViewSet

from taxonomy.models import Family, Genus, Order, Species, Subfamily, Subspecies, Tribe
from taxonomy.serializers import (
    FamilySerializer,
    GenusSerializer,
    OrderSerializer,
    SpeciesSerializer,
    SubfamilySerializer,
    SubspeciesSerializer,
    TribeSerializer,
)
from utils.helpers import get_fields


class OrdersAPIViewSet(BaseAPIViewSet):
    """A custom API view set for the Order model using the OrderSerializer."""

    base_serializer_class = OrderSerializer
    model = Order
    queryset = Order.objects.all()
    body_fields = get_fields(OrderSerializer)
    listing_default_fields = get_fields(OrderSerializer)


class FamiliesAPIViewSet(BaseAPIViewSet):
    """A custom API view set for the Family model using the FamilySerializer."""

    base_serializer_class = FamilySerializer
    model = Family
    queryset = Family.objects.select_related("order").all()
    body_fields = get_fields(FamilySerializer)
    listing_default_fields = get_fields(FamilySerializer)


class SubfamiliesAPIViewSet(BaseAPIViewSet):
    """A custom API view set for the Subfamily model using the SubfamilySerializer."""

    base_serializer_class = SubfamilySerializer
    model = Subfamily
    queryset = (
        Subfamily.objects.select_related("family").select_related("family__order").all()
    )
    body_fields = get_fields(SubfamilySerializer)
    listing_default_fields = get_fields(SubfamilySerializer)


class TribesAPIViewSet(BaseAPIViewSet):
    """A custom API view set for the Tribe model using the TribeSerializer."""

    base_serializer_class = TribeSerializer
    model = Tribe
    queryset = (
        Tribe.objects.select_related("subfamily")
        .select_related("subfamily__family")
        .select_related("subfamily__family__order")
        .all()
    )
    body_fields = get_fields(TribeSerializer)
    listing_default_fields = get_fields(TribeSerializer)


class GeneraAPIViewSet(BaseAPIViewSet):
    """A custom API view set for the Genus model using the GenusSerializer."""

    base_serializer_class = GenusSerializer
    model = Genus
    queryset = (
        Genus.objects.select_related("tribe")
        .select_related("tribe__familiy")
        .select_related("tribe__subfamily__family")
        .select_related("tribe__subfamily__family__order")
        .all()
    )
    body_fields = get_fields(GenusSerializer)
    listing_default_fields = get_fields(GenusSerializer)


class SpeciesAPIViewSet(BaseAPIViewSet):
    """A custom API view set for the Species model using the SpeciesSerializer."""

    base_serializer_class = SpeciesSerializer
    model = Species
    queryset = (
        Species.objects.select_related("genus")
        .select_related("genus__tribe")
        .select_related("genus__tribe__familiy")
        .select_related("genus__tribe__subfamily__family")
        .select_related("genus__tribe__subfamily__family__order")
        .all()
    )
    body_fields = get_fields(SpeciesSerializer)
    listing_default_fields = get_fields(SpeciesSerializer)


class SubspeciesAPIViewSet(BaseAPIViewSet):
    """A custom API view set for the Subspecies model using the SubspeciesSerializer."""

    base_serializer_class = SubspeciesSerializer
    model = Subspecies
    queryset = (
        Subspecies.objects.select_related("species")
        .select_related("species__genus")
        .select_related("species__genus__tribe")
        .select_related("species__genus__tribe__familiy")
        .select_related("species__genus__tribe__subfamily__family")
        .select_related("species__genus__tribe__subfamily__family__order")
        .all()
    )
    body_fields = get_fields(SubfamilySerializer)
    listing_default_fields = get_fields(SubfamilySerializer)
