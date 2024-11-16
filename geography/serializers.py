from rest_framework import serializers


class CountrySerializer(serializers.ModelSerializer):
    """A serializer for the Country model.

    It serializes a Country object instance's id, name, and abbr. It also serializes date_created
    and date_modified inherited from the TimeStampMixin."""

    def to_representation(self, value):
        """Overwrites the default to_representation() method to custom-format the Country data."""

        return {
            "id": value.id,
            "name": value.name,
            "abbr": value.abbr,
            "date_created": value.date_created,
            "date_modified": value.date_modified,
        }


class StateSerializer(serializers.ModelSerializer):
    """A serializer for the State model.

    It serializes a State object instance's id, name, and abbr. It also includes the id, name, and
    abbr of the Country object instance to which the State object instance belongs, as well as
    date_created and date_modified inherited from the TimeStampMixin."""

    def to_representation(self, value):
        """Overwrites the default to_representation() method to custom-format the State data."""

        return {
            "id": value.id,
            "name": value.name,
            "abbr": value.abbr,
            "date_created": value.date_created,
            "date_modified": value.date_modified,
            "country": {
                "id": value.country.id,
                "name": value.country.name,
                "abbr": value.country.abbr,
            },
        }


class CountySerializer(serializers.ModelSerializer):
    """A serializer for the County model.

    It serializes a County object instance's id, name, abbr, and full_name. It also includes the id,
    name, and abbr of both the Country object instance and the State object instnce to which the
    County object instance belongs. Also included are date_created and date_modified inherited from
    the TimeStampMixin."""

    def to_representation(self, value):
        """Overwrites the default to_representation() method to custom-format the County data."""

        return {
            "id": value.id,
            "name": value.name,
            "abbr": value.abbr,
            "full_name": value.full_name,
            "date_created": value.date_created,
            "date_modified": value.date_modified,
            "country": {
                "id": value.state.country.id,
                "name": value.state.country.name,
                "abbr": value.state.country.abbr,
            },
            "state": {
                "id": value.state.id,
                "name": value.state.name,
                "abbr": value.state.abbr,
            },
        }


class LocalitySerializer(serializers.ModelSerializer):
    """A serializer for the Locality model.

    It serializes a Locality object instance's id, name, range, and town. Depending on which region
    to which the Locality object instance belongs (Country, State, or County), the id, name, and
    abbr of that region's instance are included. Lastly, also serialized are date_created and
    date_modified inherited from the TimeStampMixin."""

    def to_representation(self, value):
        """Overwrites the default to_representation() method to custom-format the Locality data."""

        # Check for whether country, state, or county are NOT None
        county = ""
        state = ""
        country = ""

        if value.county is not None:
            county = {
                "id": value.county.id,
                "name": value.county.name,
                "abbr": value.county.abbr,
            }

        if value.state is not None:
            state = {
                "id": value.state.id,
                "name": value.state.name,
                "abbr": value.state.abbr,
            }

        if value.country is not None:
            country = {
                "id": value.country.id,
                "name": value.country.name,
                "abbr": value.country.abbr,
            }

        return {
            "id": value.id,
            "name": value.name if value.name else "",
            "range": value.range if value.range else "",
            "town": value.town if value.town else "",
            "date_created": value.date_created,
            "date_modified": value.date_modified,
            "county": county,
            "state": state,
            "country": country,
        }


class GPSSerializer(serializers.ModelSerializer):
    """A serializer for the GPS model.

    It serializes a GPS object instance's id, latitude, longitude, elevation, and elevetion_meters.
    Also included are the Locality object instance's id, name, range, and town to which the GPS
    object instance belongs, as well as date_created and date_modified inherited from the
    TimeStampMixin."""

    def to_representation(self, value):
        """Overwrites the default to_representation() method to custom-format the GPS data."""

        return {
            "id": value.id,
            "latitude": str(value.latitude) if value.latitude else "",
            "longitude": str(value.longitude) if value.longitude else "",
            "elevation": value.elevation,
            "elevation_meters": value.elevation_meters,
            "date_created": value.date_created,
            "date_modified": value.date_modified,
            "locality": {
                "id": value.locality.id,
                "name": value.locality.name,
                "range": value.locality.range,
                "town": value.locality.town,
            },
        }


class CollectingTripSerializer(serializers.ModelSerializer):
    """A serializer for the CollectingTrip model.

    It serializes a CollectingTrip object instance's id, name, slug, start_date, and end_date. It
    also includes an array of each State object instance to which this CollectingTrip belongs, with
    each State object instance's id, name, and abbr serialized. Lastly, date_created and
    date_modified inherited from the TimeStampMixin."""

    def to_representation(self, value):
        """Overwrites the default to_representation() method to custom-format the CollectingTrip
        data."""

        # Create a list to hold all of the State object instances that belong to this
        # CollectingTrip object instance
        states = []

        for state in value.states.all():
            states.append(
                {
                    "id": state.id,
                    "name": state.name,
                    "abbr": state.abbr,
                }
            )

        return {
            "id": value.id,
            "name": value.name,
            "slug": value.slug,
            "states": states,
            "start_date": str(value.start_date),
            "end_date": str(value.end_date),
            "notes": value.notes,
            "date_created": value.date_created,
            "date_modified": value.date_modified,
        }
