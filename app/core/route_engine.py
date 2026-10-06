import json


def load_routes():
    with open(
        "app/data/busroute.json",
        "r",
        encoding="utf-8"
    ) as file:
        data = json.load(file)

    return data["routes"]


def find_direct_routes(source_id, destination_id):
    routes = load_routes()

    matching_routes = []

    for route in routes:
        stops = route["stops"]

        if source_id not in stops:
            continue

        if destination_id not in stops:
            continue

        source_index = stops.index(source_id)
        destination_index = stops.index(destination_id)

        if route["route_type"] == "loop":
            matching_routes.append({
                "bus_number": route["bus_number"],
                "source": source_id,
                "destination": destination_id,
                "stops": stops,
                "source_index": source_index,
                "destination_index": destination_index
            })

        elif source_index < destination_index:
            matching_routes.append({
                "bus_number": route["bus_number"],
                "source": source_id,
                "destination": destination_id,
                "stops": stops,
                "source_index": source_index,
                "destination_index": destination_index
            })

    return matching_routes