s = input("Введите предложение: ")

a = s.split(' ')
i = len(a) - 1
t = {}
while i >= 0:
    if a[i] in t:
        i -= 1
        continue
    else:
        t[a[i]] = s.count(a[i])
        i -= 1

print("Слово и колличество повторений: " + str(t))
