from app.core.bus_eta import calculate_bus_eta


def find_earliest_bus(buses, source_latitude, source_longitude):
    earliest_bus = None

    for bus in buses:
        eta_result = calculate_bus_eta(
            bus["latitude"],
            bus["longitude"],
            source_latitude,
            source_longitude,
            bus["speed_kmph"]
        )

        if eta_result is None:
            continue

        bus_result = {
            "bus_number": bus["bus_number"],
            "distance_km": eta_result["distance_km"],
            "eta_minutes": eta_result["eta_minutes"]
        }

        if earliest_bus is None:
            earliest_bus = bus_result

        elif bus_result["eta_minutes"] < earliest_bus["eta_minutes"]:
            earliest_bus = bus_result

    return earliest_bus