def main():
	camel = input("camelCase: ")
	for letter in camel:
		if letter.isupper():
			camel = camel.replace(letter, f"_{letter.lower()}")
	print(f"snake_case: {camel}")
if __name__ == '__main__':
	main()
