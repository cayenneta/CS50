import inflect
p = inflect.engine()
name_list = []

def collect_names():
	try:
		while True:
			input_name = input("Name: ")
			name_list.append(input_name)
	except EOFError:
		return name_list

def process_names():
	names_ordered = p.join(name_list)
	print(f"\nAdieu, adieu, to {names_ordered}")

def main():
	collect_names()
	process_names()
if __name__ == '__main__':
	main()
