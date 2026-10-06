from app.core.distance_calculator import calculate_distance_km
from app.core.eta import calculate_eta


def calculate_bus_eta(
    bus_latitude,
    bus_longitude,
    source_latitude,
    source_longitude,
    bus_speed_kmph
):
    distance = calculate_distance_km(
        bus_latitude,
        bus_longitude,
        source_latitude,
        source_longitude
    )

    eta = calculate_eta(
        distance,
        bus_speed_kmph
    )

    if eta is None:
        return None

    return {
        "distance_km": distance,
        "eta_minutes": eta
    }