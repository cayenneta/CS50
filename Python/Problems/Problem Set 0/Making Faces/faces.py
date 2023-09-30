def main():
	emoticon = input ("How are you feeling? ")
	emoticon = convert(emoticon)
	print("You are feeling", emoticon)

def convert(this):
	this = this.replace(':(', '🙁')
	this = this.replace(':)', '🙂')
	return this

main()