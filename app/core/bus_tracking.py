from app.core.bus_arrival import find_earliest_bus


def find_best_bus(
    available_buses,
    bus_data_provider,
    source_latitude,
    source_longitude
):
    live_buses = []

    for bus in available_buses:
        bus_number = bus["bus_number"]

        bus_location = bus_data_provider.get_bus_location(
            bus_number
        )

        if bus_location is None:
            continue

        live_buses.append(bus_location)

    if len(live_buses) == 0:
        return None

    return find_earliest_bus(
        live_buses,
        source_latitude,
        source_longitude
    )