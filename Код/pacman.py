# Калькулятор pacman v1.1
from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()


what = input ( "Что делаем? (+,-): " )

a = float( input ("Напишите первое число: ") )
b = float( input (" Напишете второе число: ") )

if what == "+":
    c = a + b
    print( Back.GREEN )
    print( Fore.BLACK )
    print ("РЕЗУЛЬТАТ: " + str(c))
elif what == "-":
    c = a - b
    print( Back.GREEN )
    print( Fore.BLACK )
    print ("РЕЗУЛЬТАТ: " + str(c))

else:
    print ("ERROR!")

input()


