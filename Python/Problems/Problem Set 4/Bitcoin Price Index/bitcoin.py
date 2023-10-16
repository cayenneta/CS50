import requests
import sys

def float_check():
	try:
		amount = float(sys.argv[1])
	except IndexError:
		sys.exit("Missing command-line argument")
	except ValueError:
		sys.exc_info("Command-line argument is not a number")
	return amount

def get_price():
	bitcoin = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
	bitcoin = bitcoin.json()
	rate = float(bitcoin["bpi"]["USD"]["rate_float"])
	return rate

def convert(amount, rate):
	usd = amount * rate
	return usd

def main():
	amount = float_check()
	rate = get_price()
	usd = convert(amount, rate)
	print(f"${usd:,.4f}")
if __name__ == '__main__':
	main()
