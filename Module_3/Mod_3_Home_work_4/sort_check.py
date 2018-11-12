a = [1, 4, 7, 10, 11, 14, 25, 38, 58]


def sort(list, i):
    if i != 0:
        if list[i] < list[i - 1]:
            print("Список не отсортирован")
            exit(0)
        else:
            return sort(list, i - 1)


a = sort(a, len(a) - 1)
print("Список отсортирован")
