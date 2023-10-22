stock = {
            'football': 4,
            'boardgame': 10,
            'leggos': 1,
            'doll': 5 }
def fillable(stock, merch, n):
    if merch in stock.keys():
        if n <= stock[merch]:
            return True
        else:
            return False
    else :
        return False
print(fillable(stock,'leggos',2))