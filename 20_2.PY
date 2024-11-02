# 讀取輸入
total_num = int(input())
matrix_count = list(input())

num_count = total_num * total_num

# 初始化矩陣
matrix = []
current_num = 1
for i in range(total_num):
    row = []
    for j in range(total_num):
        row.append(current_num)
        current_num += 1
    matrix.append(row)

print(matrix)

# 定義旋轉函數
def rotate_clockwise(matrix):
    new_matrix = []
    for j in range(total_num):
        new_row = []
        for i in range(total_num - 1, -1, -1):
            new_row.append(matrix[i][j])
        new_matrix.append(new_row)
    return new_matrix

def rotate_counterclockwise(matrix):
    new_matrix = []
    for j in range(total_num - 1, -1, -1):
        new_row = []
        for i in range(total_num):
            new_row.append(matrix[i][j])
        new_matrix.append(new_row)
    return new_matrix

# 依序對矩陣進行旋轉
for rotation in matrix_count:
    if rotation == 'L':
        matrix = rotate_counterclockwise(matrix)
    elif rotation == 'R':
        matrix = rotate_clockwise(matrix)

# 輸出最終矩陣
for i in range(total_num):
    for j in range(total_num):
        print(matrix[i][j], end=' ')
    print()
