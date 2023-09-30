def main():
	paid = 0
	while paid < 50:
		print(f"Amount Due: {50 - paid}")
		inserted = int(input("Insert coin: "))
		if inserted not in {5, 10, 25}:
			paid = 0
		else:
			paid = paid + inserted
	print(f"Change Owed: {paid - 50}")
if __name__ == '__main__':
	main()