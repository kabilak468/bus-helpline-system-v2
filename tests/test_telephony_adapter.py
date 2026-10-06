from app.adapters.telephony.provider_adapter import ProviderAdapter


def test_welcome_message():
    provider = ProviderAdapter()

    result = provider.generate_welcome_message()

    assert result["action"] == "speak"
    assert "Welcome" in result["text"]


def test_language_menu():
    provider = ProviderAdapter()

    result = provider.generate_language_menu()

    assert result["action"] == "menu"
    assert result["options"]["1"] == "English"
    assert result["options"]["2"] == "Tamil"
    assert result["options"]["3"] == "Hindi"


def test_location_prompt():
    provider = ProviderAdapter()

    result = provider.generate_location_prompt()

    assert result["action"] == "speak"
    assert "current location" in result["text"]


def test_destination_prompt():
    provider = ProviderAdapter()

    result = provider.generate_destination_prompt()

    assert result["action"] == "speak"
    assert "destination" in result["text"]


def test_bus_response():
    provider = ProviderAdapter()

    result = provider.generate_bus_response(
        "111",
        5
    )

    assert result["action"] == "speak"
    assert "111" in result["text"]
    assert "5" in result["text"]


def test_error_response():
    provider = ProviderAdapter()

    result = provider.generate_error_response(
        "Location not recognized"
    )

    assert result["action"] == "speak"
    assert result["text"] == "Location not recognized"