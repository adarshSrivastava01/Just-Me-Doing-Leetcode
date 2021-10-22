def firstUniqChar(s):
    d = dict()
    uniqElement = None
    for each in s:
        if each in d:
            current = -abs(d[each])
            d[each] = current - 1
        else:
            d[each] = 1
    for each in d:
        if d[each] == 1:
            uniqElement = each
            break
    if uniqElement:
        return s.index(uniqElement)
    return -1


print(firstUniqChar("aabb"))
