#сортировка по возрастанию
#создаем список, обычный массив:
arr = [1, 58, 12, 96, 45, 72, 22, 59, 27 ,63, 100, 159, 7]
#вычисляем длину списка массива
n = len(arr)
#внешний цикл отсчитывает количество "проходов" по массиву
for i in range(0, n+1):
    for j in range(1, i):
        if arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
        print(j+1, "- ый проход цикла - ",end=" ")
    print(arr)
print(arr)