def lengthOfLastWord(s):
    s = s.strip()
    n = len(s)
    j = n - 1
    ans = 0
    while s[j] != " " and j >= 0:
        ans += 1
        j -= 1
    return ans


x = lengthOfLastWord("Hello World")
print(x)
