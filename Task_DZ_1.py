# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Namber = int (input("Введите день недели от 1 до 7"))

if Namber > 5 and Namber <=7:
    print ("Это выходной день в недели")
elif Namber <= 5 and Namber >=1:
    print ("Это будний день недели ")
else:
    print ("Введеное число больше или меньше заданного диапазона")
