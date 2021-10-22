def intersect(nums1, nums2):
    arr1 = [0 for _ in range(1000)]
    arr2 = [0 for _ in range(1000)]
    ans = []
    for each in nums1:
        arr1[each] += 1
    for each in nums2:
        arr2[each] += 1
    for i in range(len(arr2)):
        if arr2[i] > 0:
            ans.append()
