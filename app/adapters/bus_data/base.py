from abc import ABC, abstractmethod


class BusDataProvider(ABC):

    @abstractmethod
    def get_available_buses(self):
        pass

    @abstractmethod
    def get_bus_location(self, bus_number):
        pass