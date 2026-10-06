from app.core.conversation_manager import start_conversation


def test_valid_conversation():
    result = start_conversation(
        "1",
        "saravanampatti",
        "kumaraguru"
    )

    assert result["status"] == "success"
    assert result["language"] == "en"
    assert result["source"]["id"] == "saravanampatti"
    assert result["destination"]["id"] == "kct"


def test_tamil_conversation():
    result = start_conversation(
        "2",
        "saravanampatti",
        "kumaraguru"
    )

    assert result["status"] == "success"
    assert result["language"] == "ta"


def test_hindi_conversation():
    result = start_conversation(
        "3",
        "saravanampatti",
        "kumaraguru"
    )

    assert result["status"] == "success"
    assert result["language"] == "hi"


def test_invalid_language():
    result = start_conversation(
        "5",
        "saravanampatti",
        "kumaraguru"
    )

    assert result["status"] == "error"
    assert result["message"] == "Invalid language selection"


def test_invalid_source():
    result = start_conversation(
        "1",
        "unknownplace",
        "kumaraguru"
    )

    assert result["status"] == "error"
    assert result["message"] == "Source location not recognized"


def test_invalid_destination():
    result = start_conversation(
        "1",
        "saravanampatti",
        "unknownplace"
    )

    assert result["status"] == "error"
    assert result["message"] == "Destination location not recognized"


def test_no_matching_bus():
    result = start_conversation(
        "1",
        "gandhipuram",
        "unknownplace"
    )

    assert result["status"] == "error"


def test_conversation_with_coordinates():
    result = start_conversation(
        "1",
        "saravanampatti",
        "kumaraguru"
    )

    assert result["status"] == "success"

    assert result["source"]["id"] == "saravanampatti"
    assert result["destination"]["id"] == "kct"

    assert result["source"]["latitude"] == 11.0812
    assert result["source"]["longitude"] == 76.9986

    assert result["destination"]["latitude"] == 11.0784
    assert result["destination"]["longitude"] == 76.9989


def test_conversation_fuzzy_source():
    result = start_conversation(
        "1",
        "saravana patti",
        "kumaraguru"
    )

    assert result["status"] == "success"
    assert result["source"]["id"] == "saravanampatti"


def test_conversation_fuzzy_destination():
    result = start_conversation(
        "1",
        "saravanampatti",
        "kumaraguru college"
    )

    assert result["status"] == "success"
    assert result["destination"]["id"] == "kct"


def test_conversation_with_kct_alias():
    result = start_conversation(
        "1",
        "saravanampatti",
        "kct"
    )

    assert result["status"] == "success"
    assert result["destination"]["id"] == "kct"


def test_conversation_same_location():
    result = start_conversation(
        "1",
        "kct",
        "kct"
    )

    assert result["status"] == "success"
    assert result["source"]["id"] == "kct"
    assert result["destination"]["id"] == "kct"