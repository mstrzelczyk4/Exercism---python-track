def recite(start, take=1):
    recital = []
    for i in range(start, start - take, -1):
        if i > 2:
            recital.append(f'{i} bottles of beer on the wall, {i} bottles of beer.')
            recital.append(f'Take one down and pass it around, {i - 1} bottles of beer on the wall.')
        elif i == 2:
            recital.append("2 bottles of beer on the wall, 2 bottles of beer.")
            recital.append("Take one down and pass it around, 1 bottle of beer on the wall.")
        elif i == 1:
            recital.append("1 bottle of beer on the wall, 1 bottle of beer.")
            recital.append("Take it down and pass it around, no more bottles of beer on the wall.")
        else:
            recital.append("No more bottles of beer on the wall, no more bottles of beer.")
            recital.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
        recital.append("")
    return recital[:-1]
