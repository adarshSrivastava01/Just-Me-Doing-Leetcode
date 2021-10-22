nums = [1,2,3,2]

def sumOfUnique(nums):
    d = {}
    ans = 0
    for each in nums:
        a = d.get(each)
        if a is None:
            d[each] = 1
        else:
            d[each] += 1
    for (i,j) in d.keys():
        if j == 1:
            ans += i
    print(ans)

def sumOfUniqueTwo(nums):
    d = set()
    ans = 0
    for each in nums:
        try:
            d.remove(each)
        except:
            d.add(each)
    for each in d:
        ans += each
    print(ans)
sumOfUniqueTwo(nums)