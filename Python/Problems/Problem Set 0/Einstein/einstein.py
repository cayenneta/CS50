mass = input("m: ")
while True:
	try:
		mass = int(mass)
	except ValueError:
		print("Not an integer, try again!")
		mass = input("m: ")
	break
energy = mass * 90000000000000000
print("E: ", energy)