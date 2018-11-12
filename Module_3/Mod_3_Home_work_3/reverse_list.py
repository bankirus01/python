import random

count = int(input("Введите колличество элементов списка: "))

a = [random.randint(1, 100) for i in range(0, count)]

print("Сгенерированный список: " + str(a) + "\n \n")


def reverse(list, i):
    if i == len(list) // 2:
        return list
    a[i], a[count - 1 - i] = a[count - 1 - i], a[i]
    i += 1
    return reverse(list, i)


a = reverse(a, 0)

print("Обратно отсортированный список: " + str(a))
