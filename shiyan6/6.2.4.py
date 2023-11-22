def find_senior(lst): 
    mage = 0
    rlist = []
    for dict in lst:
        if dict['age'] >= mage:
            mage = dict['age']
    for dict in lst:
        if dict['age'] == mage:
            rlist.append(dict)
    return rlist
list1 = [
{ 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
{ 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
{ 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
{ 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
]
print(find_senior(list1))