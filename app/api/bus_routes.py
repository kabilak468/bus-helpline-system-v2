from flask import Blueprint, request, jsonify

from app.core.conversation_manager import start_conversation
from app.core.bus_tracking import find_best_bus
from app.adapters.bus_data.mock import MockBusDataProvider


bus_routes = Blueprint("bus_routes", __name__)

bus_data_provider = MockBusDataProvider()


@bus_routes.route("/find-bus", methods=["POST"])
def find_bus():

    data = request.get_json()

    language = data.get("language", "1")
    source_input = data.get("source")
    destination_input = data.get("destination")

    if not source_input or not destination_input:
        return jsonify({
            "status": "error",
            "message": "Source and destination are required"
        }), 400

    result = start_conversation(
        language,
        source_input,
        destination_input
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
        "source": result["source"],
        "destination": result["destination"],
        "bus": best_bus
    })