import random
import sys

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
	return posint_checker(input, "Level: ")

def checker():
	return posint_checker(input, "Guess: ")

def main():
	level_n = generator()
	answer = random.randint(1, level_n)
	while True:
		guess = checker()
		if guess > answer:
			print("Too large!")	
		elif guess < answer:
			print("Too small!")
		else:
			print("Just right!")
			sys.exit()

if __name__ == '__main__':
	main()
