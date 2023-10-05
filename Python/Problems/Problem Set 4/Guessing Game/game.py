import random

def posint_checker(input, text):
	while True:
		try:
			input = int(input(text))
		except:
			continue
		if input > 0:
			return input
		else:
			continue

def generator():
	posint_checker(level, "Level: ")

def checker():
	posint_checker(guess, "Guess: ")

def main():
	generator()
if __name__ == '__main__':
	main()
