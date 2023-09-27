print("pythonoo")
print("\tpython") # \t 表示制表符，作用为在输出字符串时，在字符串前加上八个空格 ？
print("\npython\nc\njava") # \n 表示换行符，作用为在输出字符串时，在字符串前换行 ？
mes = ' watermelon '
print(f"1{mes.rstrip()}1") # rstrip方法表示去除字符串右边的空白，同理lstrip表示去除字符串左边的空白，strip则是去除两端的空白
print(f"1{mes.lstrip()}1")
print(f"1{mes.strip()}1")
mes.lstrip()
mes = mes.lstrip()
print(mes)
web = 'https://4399.com'
print(web)
print(web.removeprefix('https://')) # removeprefix方法表示去除字符串的前缀，具体去除的前缀为在方法后的括号中的字符串 
print(web.removesuffix('.com')) # removesuffix方法表示去除字符串的后缀，具体规则同上