def count_developers(lst):
    num = 0
    for dic in lst:
        for c in dic:
            #遍历字典时每个键值对都会遍历一次，如果直接return num返回的值是正确数字的n倍，n为字典中键值对的数量
            if dic['continent'] == 'Europe' and dic['language'] == 'JavaScript':
                num += 1
    if num != 0:
        return num/6
    else:
        return 0
print(count_developers([
{ 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
{ 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
{ 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Europe', 'age': 35, 'language': 'HTML' },
{ 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
        ]))