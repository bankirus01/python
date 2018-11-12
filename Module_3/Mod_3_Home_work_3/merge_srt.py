import random

count = int(input("Введите колличество элементов списка: "))

a = [random.randint(1, 100) for i in range(0, count)]

print("Сгенерированный список: " + str(a) + "\n \n")


def Mergelist(a, left, b, right):
    if left >= right:
        return None
    if b < left or right < b:
        return None
    c = left
    for d in range(b + 1, right + 1):
        for i in range(c, d):
            if a[d] < a[i]:
                h = a[d]
                for k in range(d, i, -1):
                    a[k] = a[k - 1]
                a[i] = h
                c = i
                break


k = 1
while k < len(a):
    g = 0
    while g < len(a):
        z = g + k + k - 1
        f = z if z < len(a) else len(a) - 1
        Mergelist(a, g, g + k - 1, f)
        g += 2 * k
    k *= 2

print("Отсортированный список: " + str(a))
