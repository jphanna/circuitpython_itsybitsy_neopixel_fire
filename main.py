import board
import time
import random
import neopixel
from fire import Fire

pixel_pin = board.D5

# Number of neopixels in the strip
num_pixels = 8

# Set this to the number of neopixels that you want to show the fire effect on
lanterns = 2

# Changed brightness from 0.1 to brighten the effect
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)


# GAMMA CORRECTION SECTION
# COLORS THAT ARE NOT GAMMA CORRECTED
colors = {
    'RED': (255, 0, 0),
    'REDORANGE': (255, 50, 0),
    'HALLOWEENORANGE': (255, 77, 0),
    'FIREORANGE': (251, 139, 35),
    'FIREORANGE2': (227, 140, 45),
    'FIREORANGE3': (222, 120, 31),
    'ORANGE': (235, 97, 35),
    'ORANGEYELLOW': (255, 100, 0),
    'YELLOW': (255, 150, 0),
    'GREEN': (0, 255, 0),
    'CYAN': (0, 255, 255),
    'BLUE': (0, 0, 255),
    'PURPLE': (180, 0, 255),
    'DARKPURPLE': (30, 0, 95),
    'INDIGO': (75, 0, 130),
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0)
}

# Store the gamma correction table.
gamma8 = []
for i in range(0, 256):
  gamma8.append(int(pow(float(i) / float(255), 2.8) * (255 + 0.5)))

# Function to obtain a gamma corrected color.
def gammaCorrection(color):
    r, g, b = color
    return (gamma8[r], gamma8[g], gamma8[b])

# Store all gamma corrected colors.
GC_COLORS = {}
for color, rgb in colors.items():
    GC_COLORS[color] = gammaCorrection(rgb)

# END OF GAMMA CORRECTION SECTION

def bounds(rgb, min, max):
    if rgb < min:
        return min
    elif rgb > max:
        return max
    else:
        return rgb


def flicker(color, spell=False):
    ''' Changes the brightness of the color values
        to make it appear to flicker.
        USE: color is the color you need adjusted,
             spell is set to True for spell effect,
             or False for regular flicker effect. '''
    
    # Unpack color values into seperate variables
    r, g, b = color
    
    if spell == True:
        brightness = random.random()
    else:
        brightness = random.uniform(0.8, 1.0)
    
    dim_r = bounds(round(r * brightness), 0, 255)
    dim_g = bounds(round(g * brightness), 0, 255)
    dim_b = bounds(round(b * brightness), 0, 255)
    return (dim_r, dim_g, dim_b)
    

# SPELL START
fx_length = 750
fx_color = GC_COLORS['INDIGO']
    
    
def spell_fx():
    fx_cycle = 0
    pixels.fill(GC_COLORS['BLACK'])
    pixels.show()
    time.sleep(0.5)

    while fx_cycle < fx_length:
        fx_brightness = flicker(fx_color, True)
        for e in range(num_pixels):
            pixels[e] = fx_brightness
            fx_cycle = fx_cycle + 1
        pixels.show()
        lantern.flicker() # This keeps the LED lantern flickering during the spell effect
        time.sleep(random.randrange(1, 100) / 1000)
    pixels.fill(GC_COLORS['BLACK'])
    pixels.show()
    time.sleep(0.5)



pixels.fill(GC_COLORS['BLACK'])
pixels.show()
time.sleep(0.01)

lantern = Fire(7, 'lantern')

# flames = [REDORANGE, ORANGE]
GC_COLOR = GC_COLORS['FIREORANGE']

while True:
    if random.randrange(0, 1000) == 500:
        spell_fx()
    else:
        for i in range(lanterns):
            # flare = flames[random.randrange(2)]
            pixels[i] = flicker(GC_COLOR)
        pixels.show()
        # Dividing this range by the number of pixels in the effect seems to make them react better:
        time.sleep((random.randrange(25, 200) / 1000) / lanterns)

    lantern.flicker()
