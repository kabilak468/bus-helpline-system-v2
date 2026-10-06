from app.core.distance_calculator import calculate_distance_km


def test_same_location():
    result = calculate_distance_km(
        11.0000,
        76.0000,
        11.0000,
        76.0000
    )

    assert result == 0.0


def test_distance_calculation():
    result = calculate_distance_km(
        11.0000,
        76.0000,
        11.0100,
        76.0000
    )

    assert result > 0
    assert result < 2


def test_distance_rounding():
    result = calculate_distance_km(
        11.0000,
        76.0000,
        11.0001,
        76.0001
    )

    assert isinstance(result, float)
    assert result >= 0