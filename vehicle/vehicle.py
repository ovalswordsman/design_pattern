from abc import ABC, abstractmethod


# Product Interface
class Vehicle(ABC):
    @abstractmethod
    def display_details(self):
        pass