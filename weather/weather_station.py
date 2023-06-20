from observer import Observer


class WeatherStation:
    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self.observers = []

    def add_observer(self, Observer):
        self.observers.append(Observer)

    def remove_observer(self, Observer):
        self.observers.remove(Observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_weather_data(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()