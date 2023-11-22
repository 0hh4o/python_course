def shorten_number(units, base):
    def shorten(num):
        if isinstance(num, str) and num.isdigit():
            num = int(num)
            for index,unit in enumerate(units):
                if (num < base) or (index == len(units)-1):
                    return f"{num}{unit}"
                num /= base
                num = int(num)
            return f"{num}{units[-1]}"
        else:
            return str(num)
    return shorten

# 示例用法
filter1 = shorten_number(['', 'k', 'm'], 1000)
print(filter1('234324'))  # 输出 '234k'
print(filter1('32424234223'))  # 输出 '3234m'
print(filter1([1, 2, 3]))  # 输出 '[1, 2, 3]'

filter2 = shorten_number(['B', 'KB', 'MB', 'GB'], 1024)
print(filter2('32'))  # 输出 '32B'
print(filter2('2100'))  # 输出 '2KB'
print(filter2('pippi'))  # 输出 'pippi'
