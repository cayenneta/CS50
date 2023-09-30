user_input = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

if (str.lower(user_input)).replace(' ','') == ("42"):
	print("Yes")
elif (str.lower(user_input)).replace(' ','') == ("fourty-two"):
	print("Yes")
elif (str.lower(user_input)).replace(' ','') == ("fourtytwo"):
	print("Yes")
elif (str.lower(user_input)).replace(' ','') == ("forty-two"):
	print("Yes")
elif (str.lower(user_input)).replace(' ','') == ("fortytwo"):
	print("Yes")
else:
	print("No")
