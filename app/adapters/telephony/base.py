from abc import ABC, abstractmethod


class TelephonyProvider(ABC):

    @abstractmethod
    def generate_welcome_message(self, language="en"):
        pass

    @abstractmethod
    def generate_language_menu(self):
        pass

    @abstractmethod
    def generate_location_prompt(self, language="en"):
        pass

    @abstractmethod
    def generate_destination_prompt(self, language="en"):
        pass

    @abstractmethod
    def generate_bus_response(
        self,
        bus_number,
        eta_minutes,
        language="en"
    ):
        pass

    @abstractmethod
    def generate_error_response(
        self,
        message,
        language="en"
    ):
        pass