# Check if the Parenthesis are Valid

def validate(para):
    dit = {')':'(','}':'{',']':'['}
    lst = []
    for i in para:
        if i in dit.values():
            lst.append(i)
        elif i in dit.keys():
            if not lst or lst[-1] != dit[i]:
                return False
            lst.pop()
    return len(lst) == 0 
print(validate('[]'))

# or

def validate(para):
    stack = []
    match = {')':'(','}':'{',']':'['}
    for ch in para:
        if ch in match:
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack
print(validate('[]'))