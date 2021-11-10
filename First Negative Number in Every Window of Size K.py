def firstNegativeNumberInWindowOfSizeK(arr, k):
    i = 0
    j = 0
    size = len(arr)
    l = []
    lengthOfL = 0
    while j < size:
        if arr[j] < 0:
            l.append(arr[j])
            lengthOfL += 1
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            if lengthOfL == 0:
                print(0)
            else:
                print(l[0])
                if arr[i] == l[0]:
                    l.pop(0)
                    lengthOfL -= 1
            i += 1
            j += 1

arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
firstNegativeNumberInWindowOfSizeK(arr, k)