def freqAlphabets(s):
    ans = ''
    coveredTill = -1
    d = {str(num): chr(x) for (x,num) in zip(range(97,106), range(1, 10))}
    m = 10
    for i in range(106, 106+17):
        d.update({str(m)+'#': chr(i)})
        m += 1
    print(d)
    i = 0
    while i<len(s)-2:
        if s[i+2] == '#':
            ans += d[s[i:i+3]]
            coveredTill = i + 2
            i += 3
        else:
            ans += d[s[i]]
            coveredTill = i+1
            i += 1
    print(coveredTill)
    coveredTill += 1
    while coveredTill < len(s):
        ans += d[s[coveredTill]]
        coveredTill += 1
    print(ans)

freqAlphabets("26#11#418#5")