observed = '369'
lo = list (observed)
dicn = {'1':['1','2','4'],'2':['1','2','3','5'],'3':['2','3','6'],'4':['1','4','5','7'],'5':['2','4','5','6','8'],'6':['3','5','6','9'],'7':['4','7','8'],'8':['5','7','8','9','0'],'9':['6','8','9'],'0':['8','0']}
def generatepin(pin,robsvd):
    if len(robsvd) == 0:
        return [pin]
    cplace = robsvd[0]
    rplace = robsvd[1:]
    pins = []
    for num in dicn[cplace]:
        newpin = pin + num
        pins.extend(generatepin(newpin,rplace))
    return pins
print(generatepin('',observed))