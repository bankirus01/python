a = []

for i in range(1500, 3000, 1):
    if i % 7 == 0 and i % 3 != 0:
        a.append(i)

print("Числа в диапазоне от 1500 до 3000 включительно, которые делятся на 7 и не делятся на 3: " + str(a))
