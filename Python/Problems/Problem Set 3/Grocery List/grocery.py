import sys
final_list = {}
grocery_list = []
def main():
	while True:
		try:
			new_item = input()
			grocery_list.append(new_item.upper())
		except EOFError:
			for item in grocery_list:
				if not item in final_list:
					final_list[item] = 1
				else:
					final_list[item] += 1
			for key, value in sorted(final_list.items()):
				print(f"{value} {key}")
			sys.exit()
if __name__ == '__main__':
	main()
