
# circuitpython_itsybitsy_neopixels_fire
For the Adafruit ItsyBitsy M4 Express
A module to quickly set up a through-hole LED and/or neopixels strand to flicker, simulating a candle, lantern or fire light in a diorama.


## Parameters for through-hole LED
### Fire(pin, fire_type)
| Arg | Notes |
|---- | ----- |
| pin | This can be any pin allowed by the Pico that can be set as a PWM output pin. **Please, understand the pulse-width modulaton block on the Pico.**|
| fire_type | As of right now the types are: "*candle*", "*lantern*", and standard default type. |

## Usage
1. Download fire.py
2. Upload it to your ItsyBitsy M4 Express.
3. Import the module into your script (i.e. main.py):

```python
from fire import Fire
```

4. Create your object. This requires:
    1. The GPIO pin you're going to use.
    2. The type of light you want. If the type is left blank, it will just default to a built in choice.

```python
my_lantern = Fire(15, "lantern")
```

5. Using a `while True:` loop, run the `flicker()` method:

```python
while True:
    my_lantern.flicker()
```
6. Run your circuitpython script on the board!


> **Always use a current limiting resistor in your LED circuit design.**


## Parameters for neopixels
### neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
| Arg | Notes |
| ---- | ----- |
| pixel_pin | Try using pin 5 of the ItsyBitsy M4 Express. It has level shifting to 5 volts for the neopixel data.|
| num_pixels | Set this to the number of neopixels in your strand. |
| brightness | Set this to how bright you want the neopixels. |
| auto_write | Leave this set to False. |


## Usage
1. TODO
2. TODO
3. TODO

```python
TODO
```
---
### Tip
If you want a larger effect, use two, or three LEDs. Each one on it's own pin and put them close together as this article by TheArduinoGuy shows:  
[Realistic Flickering Flame Effect With Arduino and LEDs](https://www.instructables.com/Realistic-Fire-Effect-with-Arduino-and-LEDs/)

This module is a re-write of, and built upon, the idea in the Arduino "Blink Without Delay" project from the Arduino IDE, and the article above.  It was created for my personal use.
