import random
count = int(input("Введите колличество элементов массива:"))
a =[random.randint(1, 200) for i in range(0, count)]
print("Сгенерированный массив:"+str(a)+"\n \n")
for i in range(0,count, 1):
    for j in range(0, count-1, 1):
        if ((a[j] > a[j+1]) and (a[j+1] % 2 == 0)) or ((a[j] > a[j+1]) and (a[j+1] % 2 != 0) and (a[j] % 2 != 0)) \
                or ((a[j] > a[j+1]) and (a[j+1] % 2 == 0) and (a[j] % 2 == 0)):
            a[j], a[j+1] = a[j+1], a[j]
print("Отсортированный массив:"+str(a))