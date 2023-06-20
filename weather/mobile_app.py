from display_device import DisplayDevice


class MobileApp(DisplayDevice):
    def update(self, temperature, humidity, pressure):
        print("Mobile App: Temperature = {}, Humidity = {}, Pressure = {}".format(
            temperature, humidity, pressure))