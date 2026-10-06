from app.core.bus_arrival import find_earliest_bus


def test_find_earliest_bus():
    buses = [
        {
            "bus_number": "111",
            "latitude": 11.0000,
            "longitude": 76.0000,
            "speed_kmph": 30
        },
        {
            "bus_number": "222",
            "latitude": 11.0050,
            "longitude": 76.0000,
            "speed_kmph": 30
        }
    ]

    result = find_earliest_bus(
        buses,
        11.0100,
        76.0000
    )

    assert result is not None
    assert result["bus_number"] == "222"
    assert result["eta_minutes"] > 0


def test_no_valid_bus():
    buses = [
        {
            "bus_number": "111",
            "latitude": 11.0000,
            "longitude": 76.0000,
            "speed_kmph": 0
        }
    ]

    result = find_earliest_bus(
        buses,
        11.0100,
        76.0000
    )

    assert result is None


def test_empty_bus_list():
    result = find_earliest_bus(
        [],
        11.0100,
        76.0000
    )

    assert result is None