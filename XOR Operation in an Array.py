def xorOperation(n, start):
    ans = 0
    a = []
    for i in range(n):
        a.append(start+2*i)
    print(a)
    n = len(a)
    for i in range(n):
        ans = ans ^ a[i]
        print(i, '******', ans, '*****', a[i], '*****', a[i])
    return ans

print(xorOperation(4,3))