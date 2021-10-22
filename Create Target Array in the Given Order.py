nums = [0,1,2,3,4]
index = [0,1,2,2,1]

def createTargetArray(nums, index):
    target = []
    n = len(nums)
    for i in range(n):
        m = index[i]
        target = target[:m] + [nums[i]] + target[m:]
        print("*******",'   ',i, '****', target)
    return target

print(createTargetArray(nums, index))