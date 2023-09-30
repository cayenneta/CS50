def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")



def dollars_to_float(d):
	d = d.replace('$','')
	
	try:
		d = float(d)
	except ValueError:
		print("You have not inputed correctly, please input a money amount as XX.XX or $XX.XX")
		main()
	
	return d



def percent_to_float(p):
	p = p.replace('%','')
	
	try:
		p = float(p)
	except ValueError:
		print("You have not inputed correctly, please input a percentage amount from 0%\-100%\ as XX%")
		main()

	p = p / 100
	
	return p



main()