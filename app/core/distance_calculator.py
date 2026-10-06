from math import radians, sin, cos, sqrt, atan2


def calculate_distance_km(
    latitude1,
    longitude1,
    latitude2,
    longitude2
):
    """
    Calculate the distance between two GPS coordinates
    using the Haversine formula.
    """

    earth_radius_km = 6371.0

    latitude1 = radians(latitude1)
    longitude1 = radians(longitude1)
    latitude2 = radians(latitude2)
    longitude2 = radians(longitude2)

    difference_latitude = latitude2 - latitude1
    difference_longitude = longitude2 - longitude1

    a = (
        sin(difference_latitude / 2) ** 2
        + cos(latitude1)
        * cos(latitude2)
        * sin(difference_longitude / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = earth_radius_km * c

    return round(distance, 2)