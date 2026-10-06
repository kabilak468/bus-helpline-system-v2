from app.core.conversation_manager import start_conversation
from app.core.bus_tracking import find_best_bus
from app.adapters.bus_data.mock import MockBusDataProvider
from app.adapters.telephony.provider_adapter import ProviderAdapter


class IVRController:

    def __init__(self):
        self.bus_data_provider = MockBusDataProvider()
        self.telephony_provider = ProviderAdapter()

    def welcome(self):
        return {
            "welcome": self.telephony_provider.generate_welcome_message(),
            "language_menu": self.telephony_provider.generate_language_menu()
        }

    def get_location_prompt(self):
        return self.telephony_provider.generate_location_prompt()

    def get_destination_prompt(self):
        return self.telephony_provider.generate_destination_prompt()

    def find_bus(
        self,
        language,
        source,
        destination
    ):
        result = start_conversation(
            language,
            source,
            destination
        )

        if result["status"] == "error":
            return self.telephony_provider.generate_error_response(
                result["message"]
            )

        best_bus = find_best_bus(
            result["buses"],
            self.bus_data_provider,
            result["source"]["latitude"],
            result["source"]["longitude"]
        )

        if best_bus is None:
            return self.telephony_provider.generate_error_response(
                "No live bus available"
            )

        return self.telephony_provider.generate_bus_response(
            best_bus["bus_number"],
            best_bus["eta_minutes"],
            result["language"]
        )