import json

from app.adapters.bus_data.base import BusDataProvider


class MockBusDataProvider(BusDataProvider):

    def load_buses(self):
        with open(
            "app/data/buses.json",
            "r",
            encoding="utf-8"
        ) as file:
            data = json.load(file)

        return data["buses"]

    def get_available_buses(self):
        return self.load_buses()

    def get_bus_location(self, bus_number):

        buses = self.load_buses()

        for bus in buses:
            if bus["bus_number"] == bus_number:
                return {
                    "bus_number": bus["bus_number"],
                    "latitude": bus["latitude"],
                    "longitude": bus["longitude"],
                    "speed_kmph": bus["speed_kmph"]
                }

        return None