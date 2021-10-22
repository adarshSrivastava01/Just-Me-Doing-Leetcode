def windowSlidingArrayBruteForce(arr, k):
    n = len(arr)
    if n < k:
        print(False)
    max_sum = 0
    for i in range(n-k+1):
        sum = 0
        for j in range(k):
            sum += arr[i+j]
        if sum > max_sum:
            max_sum = sum
    print(max_sum)


def windowSlidingTechnique(arr, k):
    n = len(arr)
    if n < k:
        print("False")
        return -1
    window_sum = arr[:k]
    max_sum = window_sum
    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(window_sum, max_sum)
    return max_sum


def window(nums, k):
    n = len(nums)
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, n):
        window_sum = window_sum + nums[i] - nums[i-k]
        max_sum = max(window_sum, max_sum)
    return max_sum / k


print(window([1, 12, -5, -6, 50, 3], 4))
