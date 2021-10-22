def printSubsets(idx, ds, array, n):
    if idx == n:
        for each in ds:
            print(each, end=" ")
        print()
        return
    ds.append(array[idx])
    printSubsets(idx+1, ds, array, n)
    ds.pop()
    printSubsets(idx+1, ds, array, n)


if __name__ == "__main__":
    array = [1, 2, 3]
    n = len(array)
    printSubsets(0, [], array, n)
