def containsNearbyDuplicate(nums, k):
    initialMap = {}
    n = len(nums)
    for i in range(k+1):
        if nums[i] in initialMap:
            initialMap[nums[i]] += 1
        else:
            initialMap[nums[i]] = 1
    for idx in range(n-k):
        elementToBeRemoved = nums[idx]
        elementToBeAdded = nums[idx + k]
        initialMap[elementToBeRemoved] -= 1
        if elementToBeAdded in initialMap:
            initialMap[elementToBeAdded] += 1
        else:
            initialMap[elementToBeAdded] = 1
        print(initialMap)
        for value in initialMap.values():
            if value > 1:
                print("YES")
    print("False")


containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
