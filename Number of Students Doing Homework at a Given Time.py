startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4

def busyStudent(startTime, endTime, queryTime):
    cnt = 0
    for (i,j) in zip(startTime, endTime):
        if i<=queryTime and j>=queryTime:
            cnt += 1
    return cnt

print(busyStudent(startTime, endTime, queryTime))