from app.adapters.bus_data.mock import MockBusDataProvider


def test_get_available_buses():
    provider = MockBusDataProvider()

    buses = provider.get_available_buses()

    assert len(buses) == 1
    assert buses[0]["bus_number"] == "111"


def test_get_bus_location():
    provider = MockBusDataProvider()

    result = provider.get_bus_location("111")

    assert result is not None
    assert result["bus_number"] == "111"
    assert result["speed_kmph"] == 30


def test_unknown_bus():
    provider = MockBusDataProvider()

    result = provider.get_bus_location("999")

    assert result is None