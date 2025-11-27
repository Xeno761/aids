# Valid Parentheses Checker
def is_valid(s):
    stack = []
    pairs = {')':'(', ']':'[', '}':'{'}

    for ch in s:
        if ch in "([{":               # push opening bracket
            stack.append(ch)
        else:                         # check closing bracket
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return len(stack) == 0            # valid if stack empty

print(is_valid("({[]})"))
print(is_valid("([)]"))
