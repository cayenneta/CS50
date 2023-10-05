from pyfiglet import Figlet
import sys
import random
figlet = Figlet()

def init_check():
	if len(sys.argv) not in (1, 3):
		print("Invalid Usage")
		sys.exit(1)

def zero_arg():
	if len(sys.argv) == 1:
		text = input("Input: ")
		selected_font = random.choice(figlet.getFonts())
		figlet.setFont(font = selected_font)
		print(figlet.renderText(text))
		sys.exit()

def two_arg():
	if not (sys.argv[1] in ("-f", "--font")) or not (sys.argv[2] in figlet.getFonts()):
		sys.exit("WRONG INPUT FOOL")
	else:
		text = input("Input: ")
		figlet.setFont(font = sys.argv[2])
		print(figlet.renderText(text))
		sys.exit()

def main():
	init_check()
	zero_arg()
	two_arg()
if __name__ == '__main__':
	main()
