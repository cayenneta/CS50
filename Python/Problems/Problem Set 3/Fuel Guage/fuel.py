def gas_checker(fuel):
	tank = eval(fuel)
	if (tank) <= 0.1:
		return "E"	
	elif (tank) >= 0.9:
		return "F"
	else:
		return f"{int(tank*100)}%"
def main():
	try:
		print(gas_checker(input("Fraction: ")))
	except Exception as e:
		main()
if __name__ == '__main__':
	main()
