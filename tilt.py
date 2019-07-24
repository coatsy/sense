from sense_hat import SenseHat
sense = SenseHat()

# colours to paint the bubble and the background
bubble_colour = (0,0,255)
level_colour = (0, 127, 0)
almost_color = (127,127,0)
wayout_colour = (127,0,0)

# acceleration factors for level and almost level
level_threshold = 0.1
almost_threshold = 0.5

def show_level(ax, ay):
    "Shows a 2x2 blue squre on the leds based on the acceleration in the x and y dimensions"

    # draw the background based on how level we are
    if abs(ax) > almost_threshold or abs(ay) > almost_threshold:
        bg = wayout_colour
    else:
        if abs(ax) > level_threshold or abs(ay) > level_threshold:
            bg = almost_color
        else:
            bg = level_colour
    
    sense.clear(bg)

    # now draw the square to show which way to go
    if abs(ax) <= almost_threshold and abs(ay) <= almost_threshold:
        centrex = 3.5 + 4 * ax/almost_threshold
        centrey = 3.5 + 4 * ay/almost_threshold

        top = max(round(centrex) - 1, 0)
        bottom = min(round(centrex), 7)

        left = max(round(centrey) - 1, 0)
        right = min(round(centrey), 7)


        sense.set_pixel(top,left,bubble_colour)
        sense.set_pixel(top,right,bubble_colour)
        sense.set_pixel(bottom,left,bubble_colour)
        sense.set_pixel(bottom,right,bubble_colour)


while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    show_level(x,y)