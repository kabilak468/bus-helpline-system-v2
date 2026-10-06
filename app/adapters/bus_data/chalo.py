import os
import requests

from app.adapters.bus_data.base import BusDataProvider


class ChaloProvider(BusDataProvider):

    def __init__(self):
        self.base_url = os.getenv("CHALO_BASE_URL")

    def get_available_buses(self):
        """
        Get currently available buses from the Chalo provider.
        """

        if not self.base_url:
            return []

        response = requests.get(
            f"{self.base_url}/buses",
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    def get_bus_location(self, bus_number):
        """
        Get the current location of a specific bus.
        """

        if not self.base_url:
            return None

        response = requests.get(
            f"{self.base_url}/buses/{bus_number}/location",
            timeout=10
        )

        response.raise_for_status()

        return response.json()