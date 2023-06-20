from weather_station import WeatherStation
from mobile_app import MobileApp
from web_interface import WebInterface
from desktop_application import DesktopApplication


if __name__ == "__main__":
    # Create the weather station
    weather_station = WeatherStation()

    # Create display devices
    mobile_app = MobileApp()
    web_interface = WebInterface()
    desktop_app = DesktopApplication()

    # Subscribe display devices to the weather station
    weather_station.add_observer(mobile_app)
    weather_station.add_observer(web_interface)
    weather_station.add_observer(desktop_app)

    # Set the weather data
    weather_station.set_weather_data(25, 60, 1013)

    # Unsubscribe a display device
    weather_station.remove_observer(mobile_app)

    # Set new weather data
    weather_station.set_weather_data(28, 65, 1010)