def is_valid(s):
	first_digit = True
	if not 2 <= len(s) <= 6:
		return False
	if not (s[0] and s[1]).isalpha():
		return False
	for letter in s:
		if not letter.isalpha() or letter.isdigit():
			return False
	for letter in s:
		if letter.isdigit() and first_digit == True and letter == "0":
			return False
		elif letter.isdigit() and not (first_digit == True and letter == "0"):
			first_digit = True
		if letter.isdigit():
			if not s[-1].isdigit:
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
