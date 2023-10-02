def gas_checker(fuel):
	fuel = input("Fraction: ")	
	x,y = float(fuel.split("/"))
	print(x + y)	
	tank = (x/y)
	if (tank) <= 0.1:
		return "E"	
	elif (tank) >= 0.9:
		return "Y"

def main():
	while True:
		try:
		except ValueError:
			pass
if __name__ == '__main__':
	main()
