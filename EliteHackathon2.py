def checkGoodString(s):
    pass


def EliteHackathon2(s):
    cnt = 0
    p = 0
    res = []
    for i in range(len(s)):
        if s[i] == "0":
            cnt -= 1
        else:
            cnt += 1
        if cnt == 0:
            m = EliteHackathon2(s[p+1:i])
            res.append("1" + m + "0")
            p = i + 1
    res.sort(reverse=True)
    return "".join(res)
