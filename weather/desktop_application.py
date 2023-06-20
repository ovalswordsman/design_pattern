from display_device import DisplayDevice


class DesktopApplication(DisplayDevice):
    def update(self, temperature, humidity, pressure):
        print("Desktop Application: Temperature = {}, Humidity = {}, Pressure = {}".format(
            temperature, humidity, pressure))