def findRestaurant(list1, list2):
    dict1 = {}
    dict2 = {}
    for i in range(len(list1)):
        dict1[list1[i]] = i
    for i in range(len(list2)):
        dict2[list2[i]] = i
    minElement = None
    minSum = 0
    currentSum = -1
    ans = []
    for each in dict1:
        if each in dict2:
            currentSum = dict1[each] + dict2[each]
            if currentSum < minSum:
                minSum = currentSum
                minElement = each
