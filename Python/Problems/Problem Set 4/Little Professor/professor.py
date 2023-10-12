import random
x = 0
y = 0

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

def play_round(level):
		guesses = 3
		x,y = generate_integer(level)
		while guesses > 0:
			guess = int(input(f"{x} + {y} = "))
			if guess == (x + y):
				return True
			else:
				print("EEE")	
				guesses -= 1
		print(f"{x} + {y} = {x + y}")
		return False

def game(level):
	score = 0
	for i in range(10):
		if play_round(level):
			score += 1
			continue
		else:
			continue
	return score

def main():
	level = get_level()
	score = game(level)
	print(score)
if __name__ == '__main__':
	main()
