def isValid(s: str) -> bool:
    a = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            a.append(c)
        else:
            if c == ')' and (not a or a.pop() != '('):
                return False
            elif c == ']' and (not a or a.pop() != '['):
                return False
            elif c == '}' and (not a or a.pop() != '{'):
                return False
    if not a:
        return True
    else:
        return False
    
print(isValid("({)"))