from app.core.route_engine import find_direct_routes


def find_available_buses(source_id, destination_id):
    routes = find_direct_routes(
        source_id,
        destination_id
    )

    buses = []

    for route in routes:
        buses.append({
            "bus_number": route["bus_number"],
            "source": route["source"],
            "destination": route["destination"]
        })

    return buses