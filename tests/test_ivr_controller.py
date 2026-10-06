from app.core.ivr_controller import IVRController


def test_ivr_welcome():
    controller = IVRController()

    result = controller.welcome()

    assert "welcome" in result
    assert "language_menu" in result

    assert result["welcome"]["action"] == "speak"
    assert result["language_menu"]["action"] == "menu"


def test_location_prompt():
    controller = IVRController()

    result = controller.get_location_prompt()

    assert result["action"] == "speak"
    assert "current location" in result["text"]


def test_destination_prompt():
    controller = IVRController()

    result = controller.get_destination_prompt()

    assert result["action"] == "speak"
    assert "destination" in result["text"]


def test_find_bus_english():
    controller = IVRController()

    result = controller.find_bus(
        "1",
        "saravanampatti",
        "kumaraguru"
    )

    assert result["action"] == "speak"
    assert "111" in result["text"]
    assert "minute" in result["text"]


def test_find_bus_tamil():
    controller = IVRController()

    result = controller.find_bus(
        "2",
        "saravanampatti",
        "kumaraguru"
    )

    assert result["action"] == "speak"
    assert "111" in result["text"]


def test_find_bus_hindi():
    controller = IVRController()

    result = controller.find_bus(
        "3",
        "saravanampatti",
        "kumaraguru"
    )

    assert result["action"] == "speak"
    assert "111" in result["text"]


def test_invalid_source():
    controller = IVRController()

    result = controller.find_bus(
        "1",
        "unknownplace",
        "kumaraguru"
    )

    assert result["action"] == "speak"
    assert "Source location not recognized" in result["text"]


def test_invalid_destination():
    controller = IVRController()

    result = controller.find_bus(
        "1",
        "saravanampatti",
        "unknownplace"
    )

    assert result["action"] == "speak"
    assert "Destination location not recognized" in result["text"]