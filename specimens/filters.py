import django_filters as filters
from specimens.models import SpecimenRecord


class SpecimenRecordFilter(filters.FilterSet):
    """A filter set for the SpecimenRecord model.

    This filter set allows filtering of specimen records based on various fields, including
    taxonomic levels; collector, preparer, and determiner names; locality details; and other
    attributes such as date, habitat, and notes.

    Each filter supports partial matching (case-insensitive) using the 'icontains' lookup
    expression. This enables flexible querying of specimen records through the API.

    Example query parameters:
        - ?family=Papilionidae
        - ?genus=Papilio
        - ?collector_lastname=Smith
        - ?country=USA
    """

    order = filters.CharFilter(field_name="order__name", lookup_expr="icontains")
    family = filters.CharFilter(field_name="family__name", lookup_expr="icontains")
    subfamily = filters.CharFilter(
        field_name="subfamily__name", lookup_expr="icontains"
    )
    tribe = filters.CharFilter(field_name="tribe__name", lookup_expr="icontains")
    genus = filters.CharFilter(field_name="genus__name", lookup_expr="icontains")
    species = filters.CharFilter(field_name="species__name", lookup_expr="icontains")
    subspecies = filters.CharFilter(
        field_name="subspecies__name", lookup_expr="icontains"
    )
    taxon = filters.CharFilter(field_name="taxon__name", lookup_expr="icontains")
    common_name = filters.CharFilter(
        field_name="taxon__common_name", lookup_expr="icontains"
    )

    determiner_lastname = filters.CharFilter(
        field_name="determiner__last_name", lookup_expr="icontains"
    )
    determiner_firstname = filters.CharFilter(
        field_name="determiner__first_name", lookup_expr="icontains"
    )
    preparer_lastname = filters.CharFilter(
        field_name="preparer__last_name", lookup_expr="icontains"
    )
    preparer_firstname = filters.CharFilter(
        field_name="preparer__first_name", lookup_expr="icontains"
    )
    collector_lastname = filters.CharFilter(
        field_name="collector__last_name", lookup_expr="icontains"
    )
    collector_firstname = filters.CharFilter(
        field_name="collector__first_name", lookup_expr="icontains"
    )

    collecting_trip = filters.CharFilter(
        field_name="collecting_trip__name", lookup_expr="icontains"
    )
    country = filters.CharFilter(field_name="country__name", lookup_expr="icontains")
    state = filters.CharFilter(field_name="state__name", lookup_expr="icontains")
    county = filters.CharFilter(field_name="county__name", lookup_expr="icontains")
    locality = filters.CharFilter(field_name="locality__name", lookup_expr="icontains")
    gps_lat = filters.CharFilter(field_name="gps__latitude", lookup_expr="icontains")
    gps_long = filters.CharFilter(field_name="gps__longitude", lookup_expr="icontains")
    elevation = filters.CharFilter(field_name="gps__elevation", lookup_expr="icontains")

    full_date = filters.CharFilter(field_name="full_date", lookup_expr="icontains")
    method = filters.CharFilter(field_name="method", lookup_expr="icontains")
    weather = filters.CharFilter(field_name="weather", lookup_expr="icontains")
    temperature = filters.CharFilter(field_name="temperature", lookup_expr="icontains")
    time_of_day = filters.CharFilter(field_name="time_of_day", lookup_expr="icontains")
    habitat = filters.CharFilter(field_name="habitat", lookup_expr="icontains")
    notes = filters.CharFilter(field_name="notes", lookup_expr="icontains")

    class Meta:
        model = SpecimenRecord
        fields = [
            "usi",
            "order",
            "family",
            "subfamily",
            "tribe",
            "genus",
            "species",
            "subspecies",
            "determiner_lastname",
            "determiner_firstname",
            "determined_year",
            "sex",
            "stage",
            "preparer_lastname",
            "preparer_firstname",
            "preparation",
            "preparation_date",
            "labels_printed",
            "labeled",
            "photographed",
            "collecting_trip",
            "country",
            "state",
            "county",
            "locality",
            "gps_lat",
            "gps_long",
            "elevation",
            "day",
            "month",
            "year",
            "collector_lastname",
            "collector_firstname",
            "method",
            "weather",
            "temperature",
            "time_of_day",
            "habitat",
            "notes",
        ]
