# num= list(map(int, input().split())) # вводим элементы преобразуя их в числа и список
# print(num) # выводим список
# i=0 # присваиваем значение для i
# for  n in num: # создаём цикл
#   num[i]= n**2 # перебираем числа в списке и возводим в квадрат 
#   i+=1 # добавляем к i единицу, чтобы перебирать числа в списке
# print(num) # выводим наш итоговый список 

num= list(map(int, input("Введите список чисел:").split()))# вводим элементы преобразуя их в числа и список
print(num) #вывод списка
n = [i**2 for i in num] # создание генератора, который возводит числа в квадрат 
print(n) # выводим наш итоговый список  
