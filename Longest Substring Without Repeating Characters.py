def lengthOfLongestSubstring(s):
    S = list(set(s))
    print(S)
    ideal = {}
    d = {}
    for each in S:
        ideal.update({each: 0})
        d.update({each: 0})
    current_max = 0
    maxi = 0
    n = len(s)
    i = 0
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    else:
        while i < n:
            if d[s[i]] != 0:
                current_max = 1
                d = ideal
                d[s[i]] = 1
                i += 1
            else:
                d.update({s[i]: 1})
                current_max += 1
                if current_max > maxi:
                    maxi = current_max
                i += 1
    print(maxi)
    return maxi

lengthOfLongestSubstring('bbbbb')