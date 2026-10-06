from app.core.route_engine import find_direct_routes
from app.core.bus_selection import find_available_buses


def test_valid_route():
    result = find_direct_routes(
        "saravanampatti",
        "kct"
    )

    assert len(result) == 1
    assert result[0]["bus_number"] == "111"

def test_loop_route():
    result = find_direct_routes(
        "kct",
        "saravanampatti"
    )

    assert len(result) == 1
    assert result[0]["bus_number"] == "111"


def test_unknown_location():
    result = find_direct_routes(
        "unknown_place",
        "kct"
    )

    assert len(result) == 0


def test_available_bus():
    result = find_available_buses(
        "saravanampatti",
        "kct"
    )

    assert len(result) == 1
    assert result[0]["bus_number"] == "111"


def test_available_bus_on_loop_route():
    result = find_available_buses(
        "kct",
        "saravanampatti"
    )

    assert len(result) == 1
    assert result[0]["bus_number"] == "111"