from display_device import DisplayDevice


class WebInterface(DisplayDevice):
    def update(self, temperature, humidity, pressure):
        print("Web Interface: Temperature = {}, Humidity = {}, Pressure = {}".format(
            temperature, humidity, pressure))