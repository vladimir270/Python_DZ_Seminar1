#Напишите программу, которая по заданному номеру четверти, 
#показывает диапазон возможных координат точек в этой четверти (x и y)

Qarter_Namber = int(input("Введите номер четверти от 1 до 4"))

if Qarter_Namber == 1:
    print("Диапазон возможных координат = Х > 0 и Y > 0")
if Qarter_Namber == 2:
    print("Диапазон возможных координат = Х < 0 и Y > 0")
if Qarter_Namber == 3:
    print("Диапазон возможных координат = Х < 0 и Y < 0")
if Qarter_Namber == 4:
    print("Диапазон возможных координат = Х > 0 и Y < 0")
if Qarter_Namber < 1 or Qarter_Namber > 4:
    print ("Такой четверти не существует. Введите от 1 до 4")
     
     
     
    
     
    