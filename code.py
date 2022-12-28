import board
import time
import random
import neopixel
from fire import Fire


pixel_pin = board.D5
num_pixels = 8

# Set this to the number of neopixels that you want to show the fire effect on
lanterns = 2

# Changed brightness from 0.1 to brighten the effect
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

RED = (255, 0, 0)
REDORANGE = (255, 50, 0)
ORANGE = (255, 77, 0)
ORANGEYELLOW = (255, 100, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
DARKPURPLE = (30, 0, 95)
DPURPLE = (152, 29, 151)
DDPURPLE = (43, 0, 87)
INDIGO = (75, 0, 130)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def bounds(rgb, min, max):
    if rgb < min:
        return min
    elif rgb > max:
        return max
    else:
        return rgb


def flicker(color):
    # Changed brightness to make less flicker
    # Brightness = random.random() created a better open flame for fireplace or campfire
    brightness = random.uniform(0.8, 1.0)
    dim_r = bounds(round(color[0] * brightness), 0, 255)
    dim_g = bounds(round(color[1] * brightness), 0, 255)
    dim_b = bounds(round(color[2] * brightness), 0, 255)
    return (dim_r, dim_g, dim_b)

# SPELL EFFECTS SECTION
fx_length = 1000
fx_color = DDPURPLE

def fx_flash(color):
    brightness = random.random()
    dim_r = bounds(round(color[0] * brightness), 0, 255)
    dim_g = bounds(round(color[1] * brightness), 0, 255)
    dim_b = bounds(round(color[2] * brightness), 0, 255)
    return (dim_r, dim_g, dim_b)


def spell_fx():
    fx_cycle = 0
    pixels.fill(BLACK)
    pixels.show()
    time.sleep(0.5)
    
    while fx_cycle < fx_length:
        fx_brightness = fx_flash(fx_color)
        for e in range(num_pixels):
            pixels[e] = fx_brightness
            fx_cycle = fx_cycle + 1
        pixels.show()
        time.sleep(random.randrange(1, 100) / 1000)
    pixels.fill(BLACK)
    pixels.show()
    time.sleep(0.5)
# END SPELL EFFECTS

lantern = Fire(7, "lantern")


pixels.fill(BLACK)
pixels.show()
time.sleep(1)

flames = [REDORANGE, ORANGE]

while True:
    if random.randrange(0, 1000) == 500:
        spell_fx()
    else:
        for i in range(lanterns):
            flare = flames[random.randrange(2)]
            pixels[i] = flicker(flames[random.randrange(0, 2)])
        pixels.show()
        # Dividing this range by the number of pixels in the effect seems to make them react better:
        time.sleep((random.randrange(10, 100) / 1000) / lanterns)

    lantern.flicker()
