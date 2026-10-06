from app.core.bus_eta import calculate_bus_eta


def test_bus_eta():
    result = calculate_bus_eta(
        11.0000,
        76.0000,
        11.0100,
        76.0000,
        30
    )

    assert result is not None
    assert result["distance_km"] > 0
    assert result["eta_minutes"] > 0


def test_bus_eta_zero_speed():
    result = calculate_bus_eta(
        11.0000,
        76.0000,
        11.0100,
        76.0000,
        0
    )

    assert result is None


def test_bus_eta_negative_speed():
    result = calculate_bus_eta(
        11.0000,
        76.0000,
        11.0100,
        76.0000,
        -10
    )

    assert result is None