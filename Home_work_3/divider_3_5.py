count = int(input("Введите колличество элементов списка: "))

a = []

for i in range(1, count, 1):
    if i % 3 == 0 or i % 5 == 0:
        a.append(i)

print("Сгенерированный список: " + str(a))
