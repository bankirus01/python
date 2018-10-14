arr = [1, 58, 12, 96, 45, 72, 22, 59, 27 ,63, 100, 159, 7]
n = len(arr)
for i in range(n):
    indxMin=i
    for j in range (i+1, n):
        if arr[j] < arr[indxMin]:
            indxMin = j
    tpm = arr[indxMin]
    arr[indxMin] = arr[i]
    arr[i] = tpm
print(arr)