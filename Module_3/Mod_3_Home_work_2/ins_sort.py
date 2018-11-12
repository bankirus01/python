import random

count = int(input("Введите колличество элементов списка: "))

a = [random.randint(1, 100) for i in range(0, count)]

print("Сгенерированный список: " + str(a) + "\n \n")

for i in range(1, count, 1):
    tmp = a[i]
    b = i - 1
    while b >= 0:
        if tmp < a[b]:
            a[b + 1], a[b] = a[b], tmp
            b -= 1
        else:
            break

print("Отсортированный список: " + str(a))
