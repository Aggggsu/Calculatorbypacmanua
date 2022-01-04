# Py

#Python калькулятор
<br>
![py](https://img.shields.io/github/languages/count/Aggggsu/-v1.2?color=gree)
![py](https://img.shields.io/github/stars/Aggggsu/-v1.2?style=social)
<br>
![Python](https://github.com/Aggggsu/-v1.2/blob/main/image/Python.png)
<br>
Простой калькулятор на Python.

#Установка 
<br>
1.`git clone https://github.com/Aggggsu/-v1.2`
<br>
2.Дальше просто открываем файл exe.
<br>
#Код

```python
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
```

