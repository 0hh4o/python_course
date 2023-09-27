first_name = "donald"
last_name = "trumpt"
full_name = f"{first_name} {last_name}" # 这种字符串被称为f字符串，python通过把花括号内的变量替换为其值来设置字符串的格式，即设置格式字符串（format string）
print(full_name.title())
print(f"Hello,{full_name.title()}!")
message = f"fxxk u,{full_name.title()}!"
print(message)