from app.core.language_manager import get_language
from app.core.place_recognition import recognize_place
from app.core.bus_selection import find_available_buses
from app.core.bus_tracking import find_best_bus


def start_conversation(
    language_choice,
    source_input,
    destination_input
):
    language = get_language(language_choice)

    if language is None:
        return {
            "status": "error",
            "message": "Invalid language selection"
        }

    source = recognize_place(source_input)

    if source is None:
        return {
            "status": "error",
            "message": "Source location not recognized",
            "language": language
        }

    destination = recognize_place(destination_input)

    if destination is None:
        return {
            "status": "error",
            "message": "Destination location not recognized",
            "language": language
        }

    buses = find_available_buses(
        source["id"],
        destination["id"]
    )

    if len(buses) == 0:
        return {
            "status": "error",
            "message": "No suitable bus found",
            "language": language,
            "source": source,
            "destination": destination
        }

    return {
        "status": "success",
        "language": language,
        "source": source,
        "destination": destination,
        "buses": buses
    }