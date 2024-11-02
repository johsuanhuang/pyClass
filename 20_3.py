# 數字矩陣

# 給定一個正整數n，產生一個n*n的初始矩陣。
# 初始矩陣中每個元素為一個數字，
# 從1開始，由左到右、由上往下增加。例如：

# n = 4 的初始矩陣
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

# 輸入n後，需要再輸入一串由L、R組成的字串，字串由左到右進行讀取，
# 每次讀取一個字元。
# L表示將整個矩陣往逆時針轉90度，R表示將整個矩陣往順時針轉90度

# 下面是n = 4 的初始矩陣讀取到L，往逆時針翻轉90度的範例：
# 4 8 12 16
# 3 7 11 15
# 2 6 10 14
# 1 5 9 13

# 下面是n = 4 的初始矩陣讀取到R，往順時針翻轉90度的範例：
# 13 9 5 1
# 14 10 6 2
# 15 11 7 3
# 16 12 8 4

# 當字串讀取完成後，輸出翻轉後的矩陣。
# ※注意，僅需要輸出完成所有翻轉後的結果，無需顯示過程

# ------------------------------------------------------------------------------

# 輸入說明：
# 第一行：輸入一個正整數n，表示n*n的矩陣（2 <= n <= 5）
# 第二行：輸入由L、R組成的字串，長度<=10。字串由左到右讀取每個字元，
# 當讀取到L時將矩陣向逆時針翻轉90度，讀取到R時將矩陣向順時針翻轉90度。

# 輸出說明：
# 輸出一個矩陣，為初始矩陣經過翻轉後的結果。

# -----------------------------------------------------------------------------

# 範例輸入說明 1:
# 3
# # 表示一個3*3的初始矩陣，如下：
# # 1 2 3
# # 4 5 6
# # 7 8 9

# RRL
# # 表示對初始矩陣進行以下操作
# # 1. R , 向順時針轉90度
# # 7 4 1
# # 8 5 2
# # 9 6 3
# # 2. R , 向順時針轉90度
# # 9 8 7
# # 6 5 4
# # 3 2 1
# # 3. L , 向逆時針轉90度
# # 7 4 1
# # 8 5 2
# # 9 6 3

# 範例輸出說明 1:
# 7 4 1
# 8 5 2
# 9 6 3
# #此為初始矩陣經過RRL三次翻轉後的結果


total_num = int(input())
matrix_count = list(input())
# # print(matrix_count)

# total_num = 4
# RLRRRLR
# matrix_count = ['R', 'L', 'R', 'R', 'R', 'L', 'R']

num_count = total_num * total_num

def count_L_R():
    L_count = matrix_count.count('L')
    R_count = matrix_count.count('R')
    return L_count - R_count

turn = count_L_R()
print(turn)


matrix = []
for row_index in range(total_num):
    row = []
    for col_index in range(total_num):
        row.append(0)
    matrix.append(row)

# print(matrix)
# matrix = [[0 for _ in range(total_num)] for _ in range(total_num)]

# init 矩陣
value = 1
for row_index in range(total_num):
    # matrix[(i-1)//total_num][(i-1)%total_num] = i
    for col_index in range(total_num):
        matrix[row_index][col_index] = value
        value += 1


def rotate_matrix(times):
    for _ in range(abs(times)):
        if times < 0: # 逆時針
            # matrix[:] = list(map(list, zip(*matrix[::-1])))
            # 步驟1：將矩陣上下顛倒
            reversed_matrix = matrix[::-1]
            # 步驟2：轉置矩陣
            new_matrix = []
            for col_index in range(total_num):
                new_row = []
                for row in reversed_matrix:
                    new_row.append(row[col_index])
                new_matrix.append(new_row)
            # 更新
            for i in range(total_num):
                for j in range(total_num):
                    matrix[i][j] = new_matrix[i][j]
        else: # 順時針
            # matrix[:] = list(map(list, zip(*matrix)))[::-1]
            transposed_matrix = []
            for col_index in range(total_num):
                new_row = []
                for row in matrix:
                    new_row.append(row[col_index])
                transposed_matrix.append(new_row)
            new_matrix = transposed_matrix[::-1]
            # 更新
            for i in range(total_num):
                for j in range(total_num):
                    matrix[i][j] = new_matrix[i][j]

rotate_matrix(turn)
# 印矩陣
for row in matrix:
    for value in row:
        print(value, end=' ')
    print()
