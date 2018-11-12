import random

count = int(input("Введите список элементов: "))

a = [random.randint(1, 10) for i in range(0, count)]

print("Сгенерированный список: " + str(a) + "\n \n")

for i in range(0, count, 1):
    j = i + 1
    while j <= len(a) - 1:
        if a[i] == a[j]:
            a.pop(j)
        else:
            j += 1

print("Дубликаты из списка удалены: " + str(a))
