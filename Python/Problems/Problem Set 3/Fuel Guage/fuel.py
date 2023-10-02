import math

bol = True
while bol:
	frac = input("Enter a fraction (x/y): ")
	frac = frac.split("/")
	if (frac[0].isnumeric() == False or frac[1].isnumeric() == False) or (int(frac[1]) < 0) or (int(frac[0]) > int(frac[1])):
		print("Invalid input")
	else:
		bol = False
frac = [float(i) for i in frac]
frac = frac[0] / frac[1]
frac = frac*100
frac = round(frac)
if (frac >= 99):
	print("F")
elif (frac <= 1):
	print("E")
else:
	print(f"{frac}%")