count = int(input("Введите число, которое является концом списка: "))
a = []
for i in range(0, count, 1):
    if (i % 2 == 0 and i % 3 == 0) or (i % 2 != 0 and i % 7 == 0):
        a.append(i)

print("Сгенерированный список: " + str(a))
