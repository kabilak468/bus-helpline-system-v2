from flask import Blueprint, request, jsonify

from app.core.conversation_manager import start_conversation
from app.core.ivr_controller import IVRController
from app.core.bus_tracking import find_best_bus
from app.adapters.bus_data.mock import MockBusDataProvider


telephony_routes = Blueprint(
    "telephony_routes",
    __name__
)

ivr_controller = IVRController()
bus_data_provider = MockBusDataProvider()


@telephony_routes.route(
    "/conversation",
    methods=["POST"]
)
def conversation():

    data = request.get_json()

    language = data.get("language", "1")
    source = data.get("source")
    destination = data.get("destination")

    if not source or not destination:
        return jsonify({
            "status": "error",
            "message": "Source and destination are required"
        }), 400

    result = start_conversation(
        language,
        source,
        destination
    )

    if result["status"] == "error":
        return jsonify(result), 400

    best_bus = find_best_bus(
        result["buses"],
        bus_data_provider,
        result["source"]["latitude"],
        result["source"]["longitude"]
    )

    if best_bus is None:
        return jsonify({
            "status": "error",
            "message": "No live bus available"
        }), 404

    return jsonify({
        "status": "success",
        "language": result["language"],
        "source": result["source"]["name"],
        "destination": result["destination"]["name"],
        "bus_number": best_bus["bus_number"],
        "distance_km": best_bus["distance_km"],
        "eta_minutes": best_bus["eta_minutes"]
    })


@telephony_routes.route(
    "/ivr/welcome",
    methods=["POST"]
)
def ivr_welcome():

    result = ivr_controller.welcome()

    return jsonify(result)


@telephony_routes.route(
    "/ivr/location-prompt",
    methods=["POST"]
)
def ivr_location_prompt():

    result = ivr_controller.get_location_prompt()

    return jsonify(result)


@telephony_routes.route(
    "/ivr/destination-prompt",
    methods=["POST"]
)
def ivr_destination_prompt():

    result = ivr_controller.get_destination_prompt()

    return jsonify(result)


@telephony_routes.route(
    "/ivr/find-bus",
    methods=["POST"]
)
def ivr_find_bus():

    data = request.get_json()

    language = data.get("language", "1")
    source = data.get("source")
    destination = data.get("destination")

    if not source or not destination:
        return jsonify({
            "status": "error",
            "message": "Source and destination are required"
        }), 400

    result = ivr_controller.find_bus(
        language,
        source,
        destination
    )

    return jsonify(result)