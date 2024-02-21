# Калькулятор by PacMan v1.50_RC
def englishv():
	print("+ or -  \n\nAnother: \"mul\" - multiplication, \"d\" - division.")
	ask_user = input("Which command?: ")
	numberone = int(input("numberone: "))
	numbertwo = int(input("numbertwo: "))
	if ask_user == "+":
		finish = numberone + numbertwo
		print(numberone,"+",numbertwo,"=",finish)
	elif ask_user == "-":
		finish2 = numberone - numbertwo
		print(numberone,"-",numbertwo,"=",finish2)
	elif ask_user == "mul":
		mulf = numberone * numbertwo
		print(numberone,"×",numbertwo,"=",mulf)
	elif ask_user == "d":
		df = numberone / numbertwo
		print(numberone,"÷",numbertwo,"=",df)
	else:
		print("ERROR!")
def ukrv():
	print("+ - додавання, \"-\" - віднімання,\n \"mul\" - множення, \"d\" - ділення. \n Просто введіть символи чи букви.")
	ask = input("Яка дія?: ")
	onenum = int(input("Перше число: "))
	twonum = int(input("Друге число: "))
	if ask == "+":
		f = onenum + twonum
		print(onenum,"+",twonum,"=",f)
	elif ask == "-":
		f2 = onenum - twonum
		print(onenum,"-",twonum,"=",f2)
	elif ask == "mul":
		mulfukr = onenum * twonum
		print(onenum,"×",twonum,"=",mulfukr)
	elif ask == "d":
		dfukr = onenum / twonum
		print(onenum,"÷",twonum,"=",dfukr)
	else:
		print("Помилка...")
print("\t\tCalculator by PacMan\n\t\t\tv.1.50_RC")
ask_start = input("\nLanguege\"Ukr - Українська or eng - English\": ")
if ask_start == "ukr":
	ukrv()
elif ask_start == "eng":
	englishv()
else:
	print("ERRROR!")
input()