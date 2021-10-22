def checkSelfDividing(num):
    if '0' in str(num):
        return False
    if num > 0 and num < 10:
        return True
    # if num%2 == 1:
    #     for each in str(num):
    #         if int(each) % 2 == 0:
    #             return False
    # if num%2 == 0:
    #     for each in str(num):
    #         if int(each) % 2 == 1 and int(each) != 1:
    #             return False
    for each in str(num)[::-1]:
        if num%int(each) != 0:
            return False
    return True

def selfDividingNumber(left, right):
    ans = []
    for i in range(left, right+1):
        a = checkSelfDividing(i)
        if a:
            ans.append(i)
    print(ans)

selfDividingNumber(1, 22)