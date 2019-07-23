from sense_hat import SenseHat
from time import sleep

blocksize = 64

def get_pixel(i):
    "Gets the x and y values for a pixel based on its ordinal position"
    x = (i % blocksize) % 8
    y = int((i%blocksize)/8)
    if y%2==1:
        x = 7-x
    return  x, y

sense = SenseHat()

sense.clear()

white = (255,255,255)
grey1 = (191,191,191)
grey2 = (127,127,127)
grey3 = (63,63,63)
black = (0,0,0)

for y in range(0,8):
    for x in range(0,8):
        sense.set_pixel(x, y, white)
        sleep(0)

sleep(1)
sense.clear()

for i in range(0,blocksize):
    x, y = get_pixel(i)
    sense.set_pixel(x, y, white)
    x, y = get_pixel(i-1)
    sense.set_pixel(x, y, grey1)
    x, y = get_pixel(i-2)
    sense.set_pixel(x, y, grey2)
    x, y = get_pixel(i-3)
    sense.set_pixel(x, y, grey3)
    x, y = get_pixel(i-4)
    sense.set_pixel(x, y, black)
    sleep(0.25)