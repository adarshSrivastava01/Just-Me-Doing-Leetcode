def countOccurencesOfAnagram(string, pattern):
    i = 0
    hashmap = dict()
    patternSize = len(pattern)
    size = len(string)
    for each in pattern:
        if each in hashmap:
            hashmap[each] += 1
        else:
            hashmap[each] = 1
    i = 0
    j = 0
    count = len(hashmap)
    ans = 0
    while j < size:
        if string[j] in hashmap:
            hashmap[string[j]] -= 1
            if hashmap[string[j]] == 0:
                count -= 1
        if j - i + 1 < patternSize:
            j += 1
        elif j - i + 1 == patternSize:
            if count == 0:
                ans += 1
            if string[i] in hashmap:
                hashmap[string[i]] += 1
                if hashmap[string[i]] == 1:
                    count += 1
            i += 1
            j += 1
    print(ans)


string = "forxxorfxdofr"
pattern = "for"
countOccurencesOfAnagram(string, pattern)
