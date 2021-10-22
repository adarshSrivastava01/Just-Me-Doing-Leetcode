def returnMinimum(a):
    # if a[0] < a[1] and a[0] < a[2]:
    #     return 0
    # if a[1] < a[2] and a[1] < a[0]:
    #     return 1
    # if a[2] < a[0] and a[2] < a[1]:
    #     return 2
    return a.index(min(a))


def thirdMax(nums):
    l = []
    n = len(nums)
    lastVisitedIndex = -1
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums)
    cnt = 0
    for i in range(n):
        if nums[i] not in l:
            l.append(nums[i])
            lastVisitedIndex = i
            cnt += 1
            if cnt == 3:
                break
    print(l, lastVisitedIndex)
    if len(l) == 1:
        return l[0]
    if len(l) == 2:
        return max(l)
    for i in range(lastVisitedIndex+1, n):
        now_min = returnMinimum(l)
        if nums[i] > l[now_min] and nums[i] not in l:
            l[now_min] = nums[i]
    return min(l)


print(thirdMax([1, 2, 2, 5, 3, 5]))
