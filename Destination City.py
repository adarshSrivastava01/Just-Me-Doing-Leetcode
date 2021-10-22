def destCity(paths):
    frequency = {}
    for each in paths:
        if each[0] in frequency:
            frequency[each[0]] += 1
        else:
            frequency[each[0]] = 1
        if each[1] in frequency:
            frequency[each[1]] += 1
        else:
            frequency[each[1]] = 1
    lst = list(frequency.keys())[0]
    minimum = [lst, frequency[lst]]
    for (city, freq) in frequency.items():
        if freq <= minimum[1]:
            minimum[0] = city
            minimum[1] = freq
    return minimum[0]


d = [["B", "C"], ["D", "B"], ["C", "A"]]
print(destCity(d))
