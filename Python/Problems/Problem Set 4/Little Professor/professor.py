import random

def get_level():
	while True:
		try:
			level = int(input("Level: "))
			if level not in [1, 2, 3]:
				continue
			return level
		except ValueError:
			continue

def generate_integer(level):
	'''I know it looks bad, but if i did random.randint(10 ** (level - 1), (10 ** level) - 1)
	it would only do 1, 9 for level one, not 0, so yeah'''
	if level == 1:
		x = random.randint(0, 9)
		y = random.randint(0, 9)
	else:
		x = random.randint(10 ** (level - 1), (10 ** level) - 1)
		y = random.randint(10 ** (level - 1), (10 ** level) - 1)
	return x, y

def game(level):
	for i in range(10):
		guesses = 3
		x,y = generate_integer(level)
		while guesses > 0:
			guess = int(input(f"{x} + {y} = "))
			if guess == (x + y):
				break	
			else:
				print("EEE")	
				guesses -= 1
		if guess == (x + y):
			continue
		print(f"{x} + {y} = {x + y}")

def main():
	level = get_level()
	game(level)
if __name__ == '__main__':
	main()