def naughty_or_nice(data):
    for item in data:
        listitem = list(item)
        listy = [char for char in listitem if 'naughty' in char]
        ynum += listy.length()
        liste += [n for n in listitem if 'nice' in n]
        enum = liste.length()
    if ynum > enum:
        print('Nice!')
    else:
        print('Naughty!')
