import string
import random


pass_word=int(input("Enter the length of your password: "))

print('''Select the character set for password from the below mentioned choices : 
		a. Alphabets
		b. Numericals
		c. Symbols
		d. Exit''')

CHARACTER_SET= ""


while(True):
	selected_opt = (input("Please choose an alphabet - "))
	if(selected_opt == "a"):
		 CHARACTER_SET+= string.ascii_letters
	elif(selected_opt == "b"):
		CHARACTER_SET += string.digits
	elif(selected_opt == "c"):
		CHARACTER_SET += string.punctuation
	elif(selected_opt == "d"):
		break
	else:
		print("Please enter a valid option!")

password = []

for i in range(pass_word):
	randomchar = random.choice(CHARACTER_SET)
	password.append(randomchar)
print("The random password is " + "".join(password))


