import sys
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def main():
	try:
		price = float(0)
		while True:
			order = input("Item: ")
			for key, value in menu.items():
				if order.lower() == key.lower():
					price += value
					print(f"Total: ${price:.2f}")
	except EOFError:
		sys.exit()
if __name__ == '__main__':
	main()
