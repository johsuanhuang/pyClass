# 圖形繪製

# 請使用迴圈繪製4種不同的圖形
# 圖形請參考範例測資

# 菱形:兩對角線長度為N且由”*”構成的菱形
# 魚形:身體由"*"組成，是一個對角線長度皆為 N 的菱形，尾巴由"-"組成三角形，
# 三角形的最長邊(底邊)在右，頂端朝左，是一個底為(N-2)，高為((N-1)/2)的三角形

# ---------------------------------------------------

# 輸入說明 :
# 第一行，輸入整數 C，1 <= C <= 4，代表接下來要畫的圖形種類
# C=1,為第一種圖形 正三角形 (參考 範例輸出 1)
# C=2,為第二種圖形 倒三角形 (參考 範例輸出 2)
# C=3,為第三種圖形 菱形 (參考 範例輸出 9)
# C=4,為第四種圖形 魚形 (參考 範例輸出 13)

# 第二行，輸入整數 N ，0 < N < 50，代表這個圖形有N行

# 輸出說明 :
# 若N為奇數且3<=N<=49。根據輸入，畫出對應的圖形
# 若N為偶數或者N<=2或N>=50。輸出 error

# 此題不考慮C<1或C>4的情況

# ---------------------------------------------------

# 範例輸入1:
# 1
# 5

# 範例輸出 1:
# <img src=https://imgur.com/mE3IEjj.png>

# --> --------------------------------------------------

# 範例輸入2:
# 2
# 5

# 範例輸出 2:
# <img src=https://imgur.com/coDIqRt.png>

# --------------------------------------------------

pic_type = int(input())

if pic_type < 1 or pic_type > 4:
    print('error')
    exit()

N = int(input())

if N % 2 == 0 or N <= 2 or N >= 50:
    print('error')
    exit()

if pic_type == 1:
    # 正三角形
    for i in range(1, N+1):
        # 輸出 #
        for j in range(N - i):
            print('#', end='')
        # 輸出 *
        for k in range(2 * i - 1):
            print('*', end='')
        # 輸出 # 補滿
        for l in range(N - i):
            print('#', end='')
        print()
elif pic_type == 2:
    # 倒三角形
    for i in range(N, 0, -1):
        # 輸出 #
        for j in range(N - i):
            print('#', end='')
        # 輸出 *
        for k in range(2 * i - 1):
            print('*', end='')
        # 輸出 # 補滿
        for l in range(N - i):
            print('#', end='')
        print()
elif pic_type == 3:
    # 繪製菱形
    # 上半部
    for i in range(1, N//2 + 2):
        for j in range(N//2 + 1 - i):
            print(' ', end='')
        for k in range(2 * i - 1):
            print('*', end='')
        print()
    # 下半部
    for i in range(N//2, 0, -1):
        for j in range(N//2 + 1 - i):
            print(' ', end='')
        for k in range(2 * i - 1):
            print('*', end='')
        print()
elif pic_type == 4:
    # 繪製魚形
    # 菱形部分（魚身）
    for i in range(1, N//2 + 2):
        for j in range(N//2 + 1 - i):
            print(' ', end='')
        for k in range(2 * i - 1):
            print('*', end='')
        print()
    for i in range(N//2, 0, -1):
        for j in range(N//2 + 1 - i):
            print(' ', end='')
        for k in range(2 * i - 1):
            print('*', end='')
        print()
    # 尾巴部分（由 '-' 組成的三角形）
    tail_height = (N - 1) // 2
    for i in range(1, tail_height + 1):
        # 尾巴左側的空格
        for j in range(N):
            print(' ', end='')
        # 輸出 '-'
        for k in range(tail_height - i + 1):
            print('-', end='')
        print()
