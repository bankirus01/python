import random

count = int(input("Введите колличестиво элементов списка: "))

a = [random.randint(1, 100) for i in range(0, count)]

print("Сгенерированный список: " + str(a) + "\n \n")


def MergerGroup(a, left, b, right):
    if left >= right:
        return None
    if b < left or right < b:
        return None
    c = left
    for j in range(b + 1, right + 1):
        for i in range(c, j):
            if a[j] < a[i]:
                e = a[j]
                for d in range(j, i, -1):
                    a[d] = a[d - 1]
                a[i] = e
                c = i
                break


k = 1
while k < len(a):
    l = 0
    while l < len(a):
        z = l + k + k - 1
        r = z if z < len(a) else len(a) - 1
        MergerGroup(a, l, l + k - 1, r)
        l += 2 * k
    k *= 2

print("Отсортированный список: " + str(a) + "\n \n")
