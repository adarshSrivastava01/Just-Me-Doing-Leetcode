def MaximumSumSubarrayOfSizeK(arr, k):
    mx = -9999999999999
    Sum = 0
    i = 0
    j = 0
    size = len(arr)
    while j < size:
        Sum = Sum + arr[j]
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            mx = max(mx, Sum)
            Sum = Sum - arr[i]
            i += 1
            j += 1
    print(mx)


arr = [2, 5, 1, 8, 2, 9, 1]
k = 3
MaximumSumSubarrayOfSizeK(arr, k)
