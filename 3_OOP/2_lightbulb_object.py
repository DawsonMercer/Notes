class Lightbulb:
    def __init__(self, wattage: int, is_led:bool, brand_name: str, brightness: int = 0, is_on: bool = False):

        self.wattage = wattage
        self.is_led = is_led
        self.brand_name = brand_name
        self.is_on = is_on
        self.brightness = brightness

    def turn_on(self):
        self.is_on = True
        print("Lightbulb turned on")

    def turn_off(self):
        self.in_on =False
        print("lightbulb turned off")

    def to_string(self):
        print(f"Wattage: {self.wattage}\nBrand: {self.brand_name}")

    def set_brightness(self, level):
        assert 0<= level <=10, "level outside bounds"
        #level = int(input("Enter Brightness(1-10): "))
        self.brightness = level
        return print("bright level is ", self.brightness)


led_lightbulb = Lightbulb(250, True, "Phillips", 1, False)
led_lightbulb.set_brightness(9)
led_lightbulb.to_string()

