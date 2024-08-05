# RGBLED Class:

## COLOUR_MAP: A dictionary mapping colour names to their respective RGB pin states.

### Initialization: 
The __init__ method initializes the MCP23017 pins for the red, green, and blue LEDs and sets up predefined blink and solid methods using partial for each colour.

set_colour: Sets the colour of the RGB LED by turning the appropriate pins on or off based on the colour name.

off: Turns off all the LED colours.

blink: Blinks a specific colour by setting the colour, waiting for a duration, then turning it off and waiting again.

blink_between: Blinks between two colours by setting the first colour, waiting, setting the second colour, waiting, then turning off.

solid: Sets a solid colour that remains until it is changed or turned off.


### Main Loop:

The loop cycles through various colours by calling the predefined blink methods directly.

It demonstrates blinking between two colours by name.

It sets a solid colour (blue) for 2 seconds, then turns off the LED for 2 seconds.

This implementation allows you to call methods like rgb_led.solid_blue(), rgb_led.solid_off(), rgb_led.blink_red(), and rgb_led.blink_between('red', 'green') for easy and clear colour control.