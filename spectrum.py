from sense_hat import SenseHat
sense = SenseHat()

def floatmod(a, b):
	intbit = int(a/b)
	return (a - (intbit * b))

# From https://www.rapidtables.com/convert/color/hsv-to-rgb.html
def get_colour(x,y, xmax, ymax):
	"Gets the colour on a 2 D spectrum for a pixel in a grid"
	H = 360 * ((x*(ymax+1))+y)/((xmax+1)*(ymax+1))
	# print (H)
	S = 0.75
	V = 0.75

	C = V*S
	BigX = C * (1 - abs(floatmod(float(H)/float(60), 2) - 1))
	m = V-C

	if H < 60:
		Rprime = C
		Gprime = BigX
		Bprime = 0
	elif H < 120:
		Rprime = BigX
		Gprime = C
		Bprime = 0
	elif H < 180:
		Rprime = 0
		Gprime = C
		Bprime = BigX
	elif H < 240:
		Rprime = 0
		Gprime = BigX
		Bprime = C
	elif H < 300:
		Rprime = BigX
		Gprime = 0
		Bprime = C
	else:
		Rprime = C
		Gprime = 0
		Bprime = BigX

	return (int((Rprime + m) * 255), int((Gprime + m) * 255), int((Bprime + m) * 255))


for x in range(0,8):
	for y in range(0,8):
		print(get_colour(x,y, 7, 7))
		sense.set_pixel(x, y, get_colour(x,y, 7, 7))


