from sense_hat import SenseHat

sense = SenseHat()

sense.clear()

r = (255,0,0)
g = (0,255,0)

while True:
	t = round(sense.get_temperature(), 1)
	p = round(sense.get_pressure(), 1)
	h = round(sense.get_humidity(), 1)

	mess = "Temp: " + str(t) + "C  Press: " + str(p) + "hPa  Hum: " + str(h) + "%"

	if t < 18.3 or t > 26.7:
		bg = r
	else:
		bg = g

	sense.show_message(mess, scroll_speed=0.05, back_colour=bg)

