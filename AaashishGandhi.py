n = int(input())
l = [1,2,0,8,5,0,0,6]

numZeros = l.count(0)
a = [each for each in l if each != 0]
print(a)

ans = []

for each in a:
    ans.append(each)
    ans.append(0)

print(ans)