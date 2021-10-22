def sumZero(n):
    if n == 1:
        return [0]
    ans = []
    m = n//2
    for i in range(m):
        ans.append(i-m)
    for i in range(m):
        ans.append(m-i)
    if n%2 == 1:
        ans.append(0)
    return ans

print(sumZero(6))