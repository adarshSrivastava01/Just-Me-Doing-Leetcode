# INPUT -> ["1 12 sign_in", "2 13 signOut"], k = 5
def EliteHackathon1(l, maxSpan):
    sign_in_dict = {}
    sign_out_dict = {}
    ans = []
    for each in l:
        data = each.split()
        id = int(data[0])
        timestamp = int(data[1])
        method = data[2]
        if method == "sign_in":
            sign_in_dict[id] = timestamp
        elif method == "sign_out":
            sign_out_dict[id] = timestamp
    for each in sign_in_dict:
        if each in sign_out_dict:
            diff = sign_out_dict[each] - sign_in_dict[each]
            if diff < maxSpan:
                ans.append(each)
    ans = sorted(ans)
    return list(map(str, ans))
