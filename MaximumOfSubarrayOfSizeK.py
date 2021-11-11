def maximumOfSubarrayOfSizeK(arr, k):
    ans = []
    size = len(arr)
    if size < k:
        return ans
    deque = []
    i = 0
    deque.append(arr[i])
    for j in range(1, size):
        if j - i < k:
            while deque and deque[-1] < arr[j]:
                deque.pop()
            deque.append(arr[j])
        else:
            ans.append(deque[0])
            if arr[i] == deque[0]:
                deque.pop(0)
            while deque and deque[-1] < arr[j]:
                deque.pop()
            deque.append(arr[j])
            i += 1
    ans.append(deque[0])
    print(ans)


arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
maximumOfSubarrayOfSizeK(arr, k)
