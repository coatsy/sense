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

colour1 = (255,127,0)
colour2 = (191,95,0)
colour3 = (127,63,0)
colour4 = (63,31,0)
colour5 = (0,0,0)

for y in range(0,8):
    for x in range(0,8):
        sense.set_pixel(x, y, colour1)
        sleep(0)

sleep(1)
sense.clear()

while True:
  for i in range(0,blocksize):
    x, y = get_pixel(i)
    sense.set_pixel(x, y, colour1)
    x, y = get_pixel(i-1)
    sense.set_pixel(x, y, colour2)
    x, y = get_pixel(i-2)
    sense.set_pixel(x, y, colour3)
    x, y = get_pixel(i-3)
    sense.set_pixel(x, y, colour4)
    x, y = get_pixel(i-4)
    sense.set_pixel(x, y, colour5)
    sleep(0.25)