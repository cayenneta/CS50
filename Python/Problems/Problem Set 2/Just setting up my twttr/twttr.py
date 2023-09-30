def main():
	UPPERCASE = ["A", "E", "I", "O", "U"]
	text = input("Input: ")
	for letter in text:
		if (letter in UPPERCASE) or (letter.upper() in UPPERCASE):
			text = text.replace(letter, "")
	print(f"Output: {text}")
if __name__ == '__main__':
	main()
