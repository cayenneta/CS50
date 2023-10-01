def is_valid(s):
	first_digit = True
	if not 2 <= len(s) <= 6:
		return False
	if not s[:2].isalpha():
		return False
	for letter in s:
		if not letter.isalpha() or letter.isdigit():
			return False
	for letter in s:
		if letter.isdigit() and first_digit == True and letter == "0":
			return False
		if letter.isdigit():
			first_digit = False
			if not s[-1].isdigit():
				return False
	else:
		return True

def main():
	plate = input("Plate: ")
	if is_valid(plate):
		print("Valid")
	else:
		print("Invalid")
if __name__ == '__main__':
	main()
