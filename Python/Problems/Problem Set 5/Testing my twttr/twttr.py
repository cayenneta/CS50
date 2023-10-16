VOWELS = ["a", "e", "i", "o", "u"]

def shorten(message):
	for letter in message:
		if letter.lower() in VOWELS:
			message = message.replace(letter, "")
	return message

def main():
	message = input("Input: ")	
	message = shorten(message)
	print(f"Output: {message}")
if __name__ == '__main__':
	main()
