# 繪製三種不同的圖形

# N代表圖形的行數，而N (3 <= N <= 50)

# 第一種圖形為直角三角形
# 共有 N 行
# 第一行輸出1
# 第二行輸出121
# 第三行輸出12321
# 以此類推，第 i 行輸出 1… i-1 + i + i-1…1 (i 為 1~N中的任一行)
# 每一行共有2 * i - 1個數字

# 例如，當N = 5時，輸出圖形為:
# 1
# 121
# 12321
# 1234321
# 123454321

# 第二種圖形為正三角形
# 共有N行
# 第一行輸出 (N-1)個 _ + 1 + (N-1)個 _
# 第二行輸出 (N-2)個 _ + 121 + (N-2)個 _
# 第三行輸出 (N-3)個 _ + 12321 + (N-3)個 _
# 以此類推，第 i 行輸出 (N-i)個 _ + (1...i-1 + i + i-1…1) + (N-i)個 _ (i 為 1~N中的任一行)
# 每一行共有2 * N - 1個字元，包含(N-i)*2個_ 與 2 * i - 1個數字

# 例如，當N = 4時，輸出圖形為:
# ___1___
# __121__
# _12321_
# 1234321

# 第三種圖形為倒三角形
# 共有N行
# 第一行輸出 0個 _ + 1...N-1 + N + N-1…1 + 0個 _
# 第二行輸出 1個 _ + 1...N-2 + N-1 + N-2…1 + 1個_
# 第三行輸出 2個 _ + 1...N-3 + N-2 + N-3…1 + 2個 _
# 以此類推，第 i 行輸出 (i-1)個 _ + (1...N-i+1) + (N-i…1) + (i-1)個 _ (i 為 1~N中的任一行)
# 每一行共有2 * N - 1個字元，包含(i-1)*2個_ 與 (2*(N-i)+1) 個數字

# 例如，當N = 4，輸出圖形為:
# 1234321
# _12321_
# __121__
# ___1___

# ---------------------------------------------------------------------------------------

# 輸入說明 :
# 第一行，輸入整數M，1<=M<=3，代表接下來要畫的圖形種類
# M=1，為第一種圖形 直角三角形 (參考 範例輸出說明 1)
# M=2，為第二種圖形 正三角形 (參考 範例輸出說明 2)
# M=3，為第三種圖形 倒三角形 (參考 範例輸出說明 3)

# 第二行，輸入整數 N ，代表這個圖形有N行，N (3 <= N <= 50)

# 輸出說明 :
# 根據輸入，畫出對應的圖形

# 範例輸入說明 1:
# 1 (輸出第1種圖形)
# 5 (圖形行數為5)

# 範例輸出說明 1:
# 第 i 行輸出 1… i-1 + i + i-1…1 (i 為 1~N中的任一行)
# 每一行共有2 * i - 1個數字
# 1 i = 1, 第 1 行輸出 1，共有1個數字
# 121 i = 2, 第 2 行輸出 121，共有3個數字
# 12321 i = 3, 第 3 行輸出 12321，共有5個數字
# 1234321 i = 4, 第 4 行輸出 1234321，共有7個數字
# 123454321 i = 5, 第 5 行輸出 123454321，共有9個數字


pic_type = int(input())

if pic_type < 1 or pic_type > 3:
    print('error')
    exit()

N = int(input())

if  N <= 2 or N >= 50:
    print('error')
    exit()

if pic_type == 1:

    for i in range(1, N+1):
        for j in range(1,i):
          print(j, end='')
        for k in range(i, 0, -1):
          print(k, end='')
        print()

elif pic_type == 2:

      for i in range(1, N+1):
          for j in range(1, N-i+1):
              print('_', end='')
          for k in range(1, i):
              print(k, end='')
          print(i, end='')
          for l in range(i-1, 0, -1):
              print(l, end='')
          for m in range(1, N-i+1):
              print('_', end='')
          print()

elif pic_type == 3:
      
      for i in range(1, N+1):
          for j in range(1, i):
              print('_', end='')
          for k in range(1, N-i+2):
              print(k, end='')
          for l in range(N-i, 0, -1):
              print(l, end='')
          for m in range(1, i):
              print('_', end='')
          print()


# re write the code

# pic_type = 3

# if pic_type < 1 or pic_type > 3:
#     print('error')
#     exit()

# N = 5

# if  N <= 2 or N >= 50:
#     print('error')
#     exit()

# if pic_type == 1:
#     for i in range(1, N+1):
#       for j in range(1, i+1):
#           print(j, end='')
#       for h in range(i-1, 0 , -1):
#           print(h, end='')
#       print()

# elif pic_type == 2:
#     for i in range(1, N+1):
#         for g in range(N-i):
#             print('-', end='')
#         for u in range(1, i+1):
#             print(u, end='')
#         for b in range(i-1, 0, -1):
#             print(b, end='')
#         for g in range(N-i):
#             print('-', end='')
#         print()

# elif pic_type == 3:
#     for i in range(1, N+1):
#         for g in range(i-1):
#             print('-', end='')
#         for u in range(1, N-i+2):
#             print(u, end='')
#         for b in range(N-i, 0, -1):
#             print(b, end='')
#         for g in range(i-1):
#             print('-', end='')
#         print()