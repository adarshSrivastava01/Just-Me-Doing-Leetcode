def isValid(s):
    stack = []
    opens = ['(', '{', '[']
    closes = [')', '}', ']']
    sign_map = {'[': ']', '{': '}', '(': ')'}
    if s[0] in closes:
        return False
    for each in s:
        if each in opens:
            stack.insert(0, each)
        else:
            current_sign = stack[0]
            if sign_map[current_sign] != each:
                return False
            else:
                stack.pop(0)
    return True


x = isValid("()")
print(x)
