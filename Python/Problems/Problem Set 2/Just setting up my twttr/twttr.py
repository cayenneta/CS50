def main():
	UPPERCASE = ["A", "E", "I", "O", "U"]
	text = input("Input: ")
	for letter in text:
		for vowel in UPPERCASE:
			if (vowel or vowel.lower) in text:
				
if __name__ == '__main__':
	main()
