def replaceElements(arr):
    i = 0
    n = len(arr)
    if len(arr) > 1:
        while i < n-1:
            j = i+1
            maxi = arr[j]
            while j < n:
                if arr[j] > maxi:
                    maxi = arr[j]
                j += 1
            arr[i] = maxi
            i += 1
        arr[n-1] = -1
        return arr
    else:
        arr[-1] = -1
        return arr


print(replaceElements([17, 18, 5, 4, 6, 1]))


def replaceElements2(arr):
    if len(arr) == 1:
        return [-1]
    n = len(arr)
    current_max = arr[-1]
    for i in range(n-1, -1, -1):
        if arr[i] > current_max:
            arr[i] = current_max
    return arr


print(replaceElements2([17, 18, 5, 4, 6, 1]))
