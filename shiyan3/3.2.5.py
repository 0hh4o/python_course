string_ = "This website is for losers LOL!"
vowel = ['a','e','i','o','u']
liststr = [char for char in string_ if char not in vowel]
str = ''.join(liststr)
print(str)