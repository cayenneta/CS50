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
		try:
			us_date = input("Date: ")
			if "/" in us_date:
				parts = us_date.split("/")
				return parts
			elif "," in us_date:
				parts = us_date.split(" ")
				parts[1] = parts[1].replace(",","")
				parts[0] = months.index(parts[0]) + 1
				return parts
		except Exception:
			pass
	print(f"{parts[2]}-{parts[0]}-{parts[1]}")
if __name__ == '__main__':
	main()
 