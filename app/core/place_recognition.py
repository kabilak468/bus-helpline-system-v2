import json

from app.core.fuzzy_matcher import find_best_match


def load_locations():
    with open(
        "app/data/locations.json",
        "r",
        encoding="utf-8"
    ) as file:
        data = json.load(file)

    return data["locations"]


def recognize_place(user_input):
    locations = load_locations()

    result = find_best_match(
        user_input,
        locations
    )

    if result is None:
        return None

    location = result["location"]

    return {
        "id": location["id"],
        "name": location["name"],
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "score": result["score"]
    }