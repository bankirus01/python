import random

countN = int(input("Введите колличество элементов списка N: "))
countM = int(input("Введите колличество элементов списка M: "))

n = [random.randint(1, 10) for i in range(0, countN)]
m = [random.randint(1, 10) for b in range(0, countM)]
c = []
print("Сгенерированный список: ")
print(n)
print(m)

if len(n) <= len(m):
    for i in range(0, len(n), 1):
        if c.count(n[i]) > 0:
            continue
        elif m.count(n[i]) > 0:
            c.append(n[i])
else:
    for i in range(0, len(m), 1):
        if c.count(m[i]) > 0:
            continue
        elif n.count(m[i]) > 0:
            c.append(m[i])

print("Дубликаты в списках  N и M: " + str(c))
