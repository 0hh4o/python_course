def triangle(row):
    color_map = {'BB': 'B', 'BG': 'R', 'BR': 'G', 'GB': 'R', 'GG': 'G', 'GR': 'B', 'RB': 'G', 'RG': 'B', 'RR': 'R'}
    while len(row) > 1:
        row = ''.join(color_map[row[i:i+2]] for i in range(len(row) - 1))
    return row


print(triangle('RBRGBRBGGRRRBGBBBGG'))