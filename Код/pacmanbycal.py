import random as rann 
def calcuminus():
  whatminus = float(input("Перше число:")) 
  whatminus2 = float(input("Друге число:")) 
  minuscalcu = whatminus - whatminus2
  print("Результат:" + str(minuscalcu))
def pluscalcu():
  whatplus = float(input("Перше число:")) 
  whatplus2 = float(input("Друге число:")) 
  plussprogress = whatplus + whatplus2
  print("Результат:" + str(plussprogress))
def mnocalcu():
  whatmno = float(input("Перше число:")) 
  whatmno2 = float(input("Друге число:")) 
  progressmno = whatmno * whatmno2
  print("Результат:" + str(progressmno))
def delenn():
  delewhat = float(input("Перше число:")) 
  delewhat2 = float(input("Друге число:")) 
  progressdele = delewhat / delewhat2
  print("Результат:" + str(progressdele))
randommnu = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
starting = 44
while starting:
  print("Калькулятор 2.0 by PacMan :>")
  print("1 - додати, 2 - мінус, 3 - множення, 4 - ділення, 5 - рандом(нова функція :> )")
  what1 = input("/")
  if what1 == "1":
    pluscalcu()
  elif what1 == "2":
    calcuminus()
  elif what1 == "3":
    mnocalcu()
  elif what1 == "4":
    delenn()
  elif what1 == "5":
    progressran = rann.randint(100,800 )
    progressran2 = rann.randint(100,800)
    infoor = float(progressran)
    infoor2 = float(progressran2)
    vinisran = infoor + infoor2
    print("Рандом:" + str(vinisran))
    print(str(infoor) + " + " + str(infoor2) + " = " + str(vinisran))
  else:
    print("Errrrrr")
input()