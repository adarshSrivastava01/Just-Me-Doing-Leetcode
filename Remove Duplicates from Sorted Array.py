def removeDuplicates(nums):
    n = len(nums)
    if n <= 1:
        return nums
    i = 0
    j = 1
    current_max = -101
    swaps = 1
    while i < n and j < n:
        if nums[i] == nums[j]:
            if nums[j] > current_max:
                current_max = nums[j]
            i += 1
            j += 1
        elif nums[i] != nums[j] and nums[j] > current_max:
            nums[i], nums[j] = nums[j], nums[i]
            print("Happend")
            print(nums)
            swaps += 1
            if nums[j] > current_max:
                current_max = nums[j]
            i += 1
            j += 1
        elif nums[i] != nums[j] and nums[i] < current_max:
            j += 1
    print(nums)


removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
