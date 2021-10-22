def addBinary(a: str, b: str) -> str:
    maxLength = max(len(a), len(b))
    if len(a) < maxLength:
        a = "0" * (maxLength - len(a)) + a
    elif len(b) < maxLength:
        b = "0" * (maxLength - len(b)) + b
    carry = 0
    cnt = 0
    j = maxLength - 1
    ans = ""
    while j >= 0:
        if cnt == 0:
            summ = int(a[j]) + int(b[j])
            if summ == 2:
                ans = ans + "0"
                carry = 1
                cnt = 1
            elif summ == 1:
                ans = ans + "1"
                carry = 0
                cnt = 1
            else:
                ans = ans + "0"
                carry = 0
                cnt = 1
            j -= 1
        elif cnt == 1:
            aj = int(a[j])
            bj = int(b[j])
            summ = aj + bj
            if summ == 0:
                ans = str(carry) + ans
            elif summ == 1:
                if carry == 1:
                    ans = "0" + ans
                    carry = 1
                elif carry == 0:
                    ans = "1" + ans
            elif summ == 2:
                if carry == 0:
                    ans = "0" + ans
                    carry = 1
                elif carry == 1:
                    ans = "1" + ans
            j -= 1
        if carry == 1:
            ans = "1" + ans
        return ans


print(addBinary("11", "01"))
