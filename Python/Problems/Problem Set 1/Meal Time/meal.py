def convert(time):
	time = time.split(":")
	hours = float(time[0])
	minutes = float(time[1])
	minutes = minutes / 60
	dec_time = hours + minutes
	return dec_time

def main():
	time = input("What time is it? ")
	dec_time = convert(time)
	if 7 <= dec_time <= 8:
		print("breakfast time")
	elif 12 <= dec_time <= 13:
		print("lunch time")
	elif 18 <= dec_time <= 19:
		print("dinner time")
if __name__ == '__main__':
	main()
