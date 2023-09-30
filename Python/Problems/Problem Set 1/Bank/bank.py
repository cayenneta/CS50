teller_greeting_init = input("Hey, I need to do some fancy bank stuff\n")
teller_greeting_manip = str.lower(teller_greeting_init)
teller_greeting_manip = teller_greeting_manip.replace(' ','')
if (teller_greeting_manip[0] == 'h') and ('hello' not in teller_greeting_manip):
	print('$20')
elif 'hello' in teller_greeting_manip:
	print('$0')
else:
	print('$100')