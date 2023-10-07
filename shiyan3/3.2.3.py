def valid_braces(string):
    stack = []
    for char in string:
        if char in "([{":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if (char == ")" and top != "(") or (char == "}" and top != "{") or (char == "]" and top != "["):
                return False
    return len(stack) == 0
valid_braces("{]}")
print(1)