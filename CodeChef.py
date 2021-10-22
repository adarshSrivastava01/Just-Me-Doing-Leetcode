# T = int(input())
# for _ in range(T):
#     N, K = list(map(int, input().split()))
#     if N - K == 1:
#         print(-1)
#     else:
#         ans = []
#         i = 1
#         while i <= K:
#             ans.append(i)
#             i += 1
#         i -= 1
#         for j in range(N, i, -1):
#             ans.append(j)
#         if (N-K) % 2 != 0:
#             m = K + (N-K)//2
#             ans[m], ans[m+1] = ans[m+1], ans[m]
#         for i in range(len(ans)):
#             print(ans[i], end=" ")
#         print()


# cook your dish here
import sys
T = int(input())
for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    odds = evens = 0
    for each in L:
        if each % 2 == 0:
            evens += 1
        else:
            odds += 1
    if evens != N:
        print(0)
    else:
        ans = pow(10, 9)
        for idx in range(N):
            a = 0
            while L[idx] % 2 != 1:
                L[idx] = L[idx] // 2
                a += 1
            if a < ans:
                ans = a
        print(ans)