def is_pangram(s):
    pangram = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
    p = set()
    for char in s:
        if char.isalpha():
            p.add(char.title())
    if p == pangram:
        return True
    else:
        return False
print(is_pangram('The quik, brown fox jumps over the lazy dog!'))