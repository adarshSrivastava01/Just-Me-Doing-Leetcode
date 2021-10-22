def lengthOfLongestSubstring(s):
    a = {}
    for each in s:
        if each in a:
            a[each] += 1
        else:
            a[each] = 1
    if len(list(a.keys())) == 1:
        return 1
    current_maximum = 0
    maximum = 0
    i = 0
    j = 0
    temp = {}
    n = len(s)
    while i < n and j < n:
        if s[j] not in temp:
            temp[s[j]] = 1
            j += 1
            current_maximum += 1
            maximum = max(current_maximum, maximum)
        else:
            temp[s[j]] -= 1
            i += 1
            j = i
            current_maximum = 1
            maximum = max(current_maximum, maximum)
            temp = {}
            temp[s[j]] = 1
            j += 1
    return maximum


print(lengthOfLongestSubstring("bbbb"))
