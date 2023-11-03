def validate_sudoku(board):
    #检查是否含有0
    for list in board:
        for num in list:
            if num == 0:
                return False
    
    # 检查行
    for row in board:
        if not is_valid_row(row):
            return False
    
    # 检查列
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_row(column):
            return False
    
    # 检查3x3子网格
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [board[row][col] for row in range(i, i+3) for col in range(j, j+3)]
            if not is_valid_row(subgrid):
                return False
    
    return True

def is_valid_row(row):
    # 统计每个数字的出现次数
    count = [0] * 10
    for num in row:
        count[num] += 1
    
    # 检查是否有任何数字出现超过一次
    for i in range(1, 10):
        if count[i] > 1:
            return False
    
    return True
