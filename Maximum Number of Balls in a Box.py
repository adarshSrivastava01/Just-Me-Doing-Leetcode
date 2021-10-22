def sumOfDigits(x):
    s = 0
    while x != 0:
        d = x % 10
        s += d
        x = x//10
    return s


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = dict()
        for i in range(lowLimit, highLimit+1):
            x = sumOfDigits(i)
            if d.get(x) != None:
                d.update({x: d.get(x)+1})
            else:
                d.update({x: 1})
        return max(list(d.values()))
