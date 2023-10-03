import sys
months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]

def main():
	while True:
		us_date = input("Date: ")
		if "/" in us_date:
			parts = us_date.split("/")
			if any(char.isalpha() for string in parts for char in string):
				continue
			for i in range(len(parts)):
				parts[i] = parts[i].replace(" ","")
			for i in range(2):
				if len(str(parts[i])) == 1:
					parts[i] = f"0{parts[i]}"
			if (not int(parts[0]) <= 12) or (not int(parts[1]) <= 31):
				continue
			print(f"{parts[2]}-{parts[0]}-{parts[1]}")
			sys.exit()
		elif "," in us_date:
			parts = us_date.split(" ")
			parts[1] = parts[1].replace(",","")
			try:
				parts[0] = months.index(parts[0].lower()) + 1
			except ValueError:
				continue
			if (not int(parts[0]) <= 12) or (not (int(parts[2]) <= 31)):
				continue
			for i in range(2):
				if len(str(parts[i])) == 1:
					parts[i] = f"0{parts[i]}"
			print(f"{parts[2]}-{parts[0]}-{parts[1]}")
			sys.exit()
		else:
			pass
if __name__ == '__main__':
	main()
 