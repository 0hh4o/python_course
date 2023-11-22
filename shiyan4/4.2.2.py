observed = '369'
#所有相邻数的字典，键是观察到的数字，值是可能是密码的数字
dicn = {'1':['1','2','4'],'2':['1','2','3','5'],'3':['2','3','6'],'4':['1','4','5','7'],'5':['2','4','5','6','8'],'6':['3','5','6','9'],'7':['4','7','8'],'8':['5','7','8','9','0'],'9':['6','8','9'],'0':['8','0']}
def generatepin(pin,robsvd):
    #当遍历完了之后就输出结果的列表
    if len(robsvd) == 0:
        return [pin]
    #cplace表示当前要处理的数字位
    cplace = robsvd[0]
    #rplace通过[1:]的方法去掉字符串的第一位
    rplace = robsvd[1:]
    #定义一个空列表
    pins = []
    #遍历字典，找到对应的可能是密码的数字
    for num in dicn[cplace]:
        newpin = pin + num
        pins.extend(generatepin(newpin,rplace))
    return pins
print(generatepin('',observed))