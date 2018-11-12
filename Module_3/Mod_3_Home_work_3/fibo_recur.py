num = int(input("Введите число: "))
a = []


def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


while num > 0:
    a.append(fibo(num))
    num -= 1

print("Сгенерированная последовательность: " + str(a[::-1]))
