import json

from app.core.fuzzy_matcher import find_best_match
from app.core.place_recognition import recognize_place


def load_locations():
    with open("app/data/locations.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return data["locations"]


def test_saravanampatti():
    locations = load_locations()

    result = find_best_match("saravanampaty", locations)

    assert result is not None
    assert result["location"]["id"] == "saravanampatti"


def test_kumaraguru():
    locations = load_locations()

    result = find_best_match("kumaraguru", locations)

    assert result is not None
    assert result["location"]["id"] == "kct"


def test_gandhipuram():
    result = recognize_place("gandhi puram")

    assert result is not None
    assert result["id"] == "gandhipuram"
    assert result["name"] == "Gandhipuram"


def test_unknown_place():
    result = recognize_place("some random place xyz")

    assert result is None