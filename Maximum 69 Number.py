def maximum69Number(num):
    ans = ''
    i = 0
    n = len(num)
    cnt = 0
    for i in range(n):
        if num[i] == '6':
            # print(ans)
            # print("Came Here")
            ans += '9'
            # print(ans)
            cnt = 1
            break
        elif num[i] == '9':
            ans = ans + '9'
    if cnt == 1:
        ans = ans + num[i+1:]
    return ans

print(maximum69Number('9996'))