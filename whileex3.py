while True:
	H = input('entre hours: ')
	R = input('entre rate: ')
	try:
		H = float(H)
		R = float(R)
		break
	except:
		print("Error, please entre numeric input")
if H <= 40:
	P = H * R
else:
	P = 40*R + ((H-40)*1.5*R)
print("Pay =", P)