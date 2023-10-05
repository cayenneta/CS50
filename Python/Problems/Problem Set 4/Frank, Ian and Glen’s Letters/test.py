from pyfiglet import Figlet
import random
figlet = Figlet()

selected_font = random.choice(figlet.getFonts())
print(selected_font)