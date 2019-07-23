from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

yellow = (255, 255, 0)
blue = (0, 0, 255)
black = (0,0,0)
white = (255,255,255)

sense.show_message("I Win", text_colour=yellow, back_colour=blue)

sense.clear(black)

r = (255,0,0)
g = (0,255,0)
b = (0,0,255)

creeper_pixels = [
	g,g,g,g,g,g,g,g,
	g,g,g,g,g,g,g,g,
	g,b,b,g,g,b,b,g,
	g,b,b,g,g,b,b,g,
	g,g,g,b,b,g,g,g,
	g,g,b,b,b,b,g,g,
	g,g,b,b,b,b,g,g,
	g,g,b,g,g,b,g,g
]

sense.set_pixels(creeper_pixels)

while True:
	sleep(1)
	sense.flip_v()
