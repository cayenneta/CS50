def gas_checker(fuel):
	float(x,y) = fuel.split("/")
	tank = (x/y)
	if (tank) <= 0.1:
		return "E"	
	elif (tank) >= 0.9:
		return "Y"

def main():
	while True:
		try: gas_checker(input("Fraction: "))
		except (ValueError, ZeroDivisionError):
			pass	
if __name__ == '__main__':
	main()
