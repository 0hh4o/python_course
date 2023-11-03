def find_outlier(integers):
    evencount = 0
    oddcount =0
    for inte in integers:
        if inte % 2 == 1:
            oddcount += 1
        else:
            evencount += 1
    if oddcount == 1:
        for inte in integers:
            if inte % 2 == 1:
                return inte
    else:
        for inte in integers:
            if inte % 2 == 0:
                return inte
print(find_outlier([1,2,4,6]))