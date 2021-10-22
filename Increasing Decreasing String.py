def sortString(s):
    hashMap = [0 for _ in range(26)]
    for each in s:
        hashMap[ord(each)-97] += 1
    answer = ""
    visited = 0
    while visited <= len(s):
        for i in range(len(hashMap)):
            if hashMap[i] > 0:
                answer += chr(97+i)
                hashMap[i] -= 1
        for i in range(25, -1, -1):
            if hashMap[i] > 0:
                answer += chr(97+i)
                hashMap[i] -= 1
        visited += 1
    print(answer)


sortString("leetcode")
