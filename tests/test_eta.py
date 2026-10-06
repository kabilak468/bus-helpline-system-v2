from app.core.eta import calculate_eta


def test_eta_calculation():
    result = calculate_eta(3, 30)

    assert result == 6


def test_eta_with_zero_speed():
    result = calculate_eta(3, 0)

    assert result is None


def test_eta_with_negative_speed():
    result = calculate_eta(3, -10)

    assert result is None


def test_eta_rounding():
    result = calculate_eta(5, 40)

    assert result == 8