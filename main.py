import time
import board
import busio
import digitalio
from adafruit_mcp230xx.mcp23017 import MCP23017
from functools import partial

class RGBLED:
    COLOUR_MAP = {
        'red': (True, False, False),
        'green': (False, True, False),
        'blue': (False, False, True),
        'yellow': (True, True, False),
        'cyan': (False, True, True),
        'magenta': (True, False, True),
        'white': (True, True, True),
        'off': (False, False, False)
    }

    def __init__(self, mcp, red_pin, green_pin, blue_pin):
        self.red = mcp.get_pin(red_pin)
        self.green = mcp.get_pin(green_pin)
        self.blue = mcp.get_pin(blue_pin)
        
        self.red.switch_to_output(value=False)
        self.green.switch_to_output(value=False)
        self.blue.switch_to_output(value=False)
        
        self.blink_red = partial(self.blink, 'red')
        self.blink_green = partial(self.blink, 'green')
        self.blink_blue = partial(self.blink, 'blue')
        self.blink_yellow = partial(self.blink, 'yellow')
        self.blink_cyan = partial(self.blink, 'cyan')
        self.blink_magenta = partial(self.blink, 'magenta')
        self.blink_white = partial(self.blink, 'white')
        self.blink_off = partial(self.blink, 'off')
        
        self.solid_red = partial(self.solid, 'red')
        self.solid_green = partial(self.solid, 'green')
        self.solid_blue = partial(self.solid, 'blue')
        self.solid_yellow = partial(self.solid, 'yellow')
        self.solid_cyan = partial(self.solid, 'cyan')
        self.solid_magenta = partial(self.solid, 'magenta')
        self.solid_white = partial(self.solid, 'white')
        self.solid_off = partial(self.solid, 'off')
    
    def set_colour(self, colour):
        red, green, blue = self.COLOUR_MAP[colour]
        self.red.value = red
        self.green.value = green
        self.blue.value = blue
    
    def off(self):
        self.set_colour('off')
    
    def blink(self, colour, duration=0.5):
        self.set_colour(colour)
        time.sleep(duration)
        self.off()
        time.sleep(duration)

    def blink_between(self, colour1, colour2, duration=0.5):
        self.set_colour(colour1)
        time.sleep(duration)
        self.set_colour(colour2)
        time.sleep(duration)
        self.off()
        time.sleep(duration)

    def solid(self, colour):
        self.set_colour(colour)

# Initialize I2C bus and MCP23017
i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c)

# Create an RGB LED object with pins 0, 1, and 2 for red, green, and blue respectively
rgb_led = RGBLED(mcp, 0, 1, 2)

# Main loop
while True:
    # Blink red
    rgb_led.blink_red()
    
    # Blink green
    rgb_led.blink_green()
    
    # Blink blue
    rgb_led.blink_blue()
    
    # Blink yellow (red + green)
    rgb_led.blink_yellow()
    
    # Blink cyan (green + blue)
    rgb_led.blink_cyan()
    
    # Blink magenta (red + blue)
    rgb_led.blink_magenta()
    
    # Blink white (red + green + blue)
    rgb_led.blink_white()
    
    # Blink between red and green
    rgb_led.blink_between('red', 'green')
    
    # Set solid colour to blue
    rgb_led.solid_blue()
    time.sleep(2)  # Keep the solid colour for 2 seconds
    
    # Turn off the LED
    rgb_led.solid_off()
    time.sleep(2)  # Keep the LED off for 2 seconds
