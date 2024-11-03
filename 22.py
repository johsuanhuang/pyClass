# 梭哈比大小

# 1.由N(2<=N<=5，N為整數)個玩家依序輪流拿牌。
# 2.每人拿五張，結果依牌型由大到小輸出玩家名稱和其牌型編號，
# 若牌型相同，依據輸入順序輸出。
# 3.每張牌由牌面與花色組成，牌面與花色的表示如下：
# 牌面： A、2~10、J、Q、K
# 花色：S (Spade,黑桃),H (Heart,紅心),D (Diamond,方塊), C (Club,梅花)
# 例如：7S 表示黑桃7

# 4.牌型編號(編號越大代表牌型越大)：
# (1) High Card : 單一張牌。
# (2) One pair: 兩張牌數字一樣
# (3) Two pairs : 兩組 Pair 的牌。
# (4) Three of a kind : 三張牌數字一樣。
# (5) Straight : 數字連續的五張牌，頭尾相接亦視為Straight。
# 例如[2, 3, 4, 5, 6],..,[Q,K , A, 2, 3], [K , A, 2, 3, 4], 
# [A, 2, 3, 4, 5]。
# (6) Flush : 五張同一花色的牌
# (7) Full House : Three of a Kind 加一個 Pair
# (8) Four of a kind: : 四張牌數字一樣
# (9) Straight flush : 數字連續的五張牌且花色一樣

# 【輸入說明】
# 第1行，輸入整數N(2<=N<=5)
# 第2~1 +N行 輸入一字串，包含英文姓名和五張牌，中間以空格格開

# 範例輸入說明：
# 2（N=2，玩家人數為整數2）
# Allen 3H 4H 5H 6H 7H（玩家Allen 紅心3 紅心4 紅心5 紅心 6 紅心7）
# Kate 9H 9D 9C 2S AS（玩家Kate 紅心9 方塊9 梅花9 黑桃2 黑桃A）

# 【輸出說明】
# 若所有牌不重複且輸入正確（參考 測試資料一）
# 則依牌型由大到小輸出玩家名稱和其牌型編號，中間以空格隔開。
# 若牌型相同，依據玩家輸入順序輸出。
# 第一行 牌型最大的玩家姓名+” ”+玩家牌型編號
# 第二行 牌型第二大的玩家姓名+” ”+玩家牌型編號
# 第N行 牌型最小的玩家姓名+” ”+玩家牌型編號

# 範例輸出說明:
# Allen 9 （玩家Allen 對應牌型為編號9的Straight flush）
# Kate 4 （玩家Kate 對應牌型為編號4的Three of a kind）

# 【特別要求】
# 1.如果一副牌中有不合法的輸入，像是不存在的牌面、花色，則輸出 
# "Error input"(參考 測試資料二)
# 2. 如果一副牌中有重複的牌出現，即一副牌當中有兩張以上牌面跟花色一模一樣，
# 則輸出"Duplicate deal"(參考 測試資料三）
# 3. 如果"Error input"和"Duplicate deal"同時發生，
# 則輸出"Error input"(參考 測試資料四)

# 【測試資料一】
# 輸入:
# 4
# Gery 6D 7C 7S 3H 10S
# Mandy 4H 4D 4C 2D 4S
# Tommy QH KD AC 5D 3S
# Nina 10D 8C 8S 8H 10H
# 輸出:
# Mandy 8
# Nina 7
# Gery 2
# Tommy 1梭哈比大小

# 1.由N(2<=N<=5，N為整數)個玩家依序輪流拿牌。
# 2.每人拿五張，結果依牌型由大到小輸出玩家名稱和其牌型編號，若牌型相同，
# 依據輸入順序輸出。
# 3.每張牌由牌面與花色組成，牌面與花色的表示如下：
# 牌面： A、2~10、J、Q、K
# 花色：S (Spade,黑桃),H (Heart,紅心),D (Diamond,方塊), C (Club,梅花)
# 例如：7S 表示黑桃7

# 4.牌型編號(編號越大代表牌型越大)：
# (1) High Card : 單一張牌。
# (2) One pair: 兩張牌數字一樣
# (3) Two pairs : 兩組 Pair 的牌。
# (4) Three of a kind : 三張牌數字一樣。
# (5) Straight : 數字連續的五張牌，頭尾相接亦視為Straight。
# 例如[2, 3, 4, 5, 6],..,[Q,K , A, 2, 3], [K , A, 2, 3, 4], 
# [A, 2, 3, 4, 5]。
# (6) Flush : 五張同一花色的牌
# (7) Full House : Three of a Kind 加一個 Pair
# (8) Four of a kind: : 四張牌數字一樣
# (9) Straight flush : 數字連續的五張牌且花色一樣

# 【輸入說明】
# 第1行，輸入整數N(2<=N<=5)
# 第2~1 +N行 輸入一字串，包含英文姓名和五張牌，中間以空格格開

# 範例輸入說明：
# 2（N=2，玩家人數為整數2）
# Allen 3H 4H 5H 6H 7H（玩家Allen 紅心3 紅心4 紅心5 紅心 6 紅心7）
# Kate 9H 9D 9C 2S AS（玩家Kate 紅心9 方塊9 梅花9 黑桃2 黑桃A）

# 【輸出說明】
# 若所有牌不重複且輸入正確（參考 測試資料一）
# 則依牌型由大到小輸出玩家名稱和其牌型編號，中間以空格隔開。若牌型相同，
# 依據玩家輸入順序輸出。
# 第一行 牌型最大的玩家姓名+” ”+玩家牌型編號
# 第二行 牌型第二大的玩家姓名+” ”+玩家牌型編號
# 第N行 牌型最小的玩家姓名+” ”+玩家牌型編號

# 範例輸出說明:
# Allen 9 （玩家Allen 對應牌型為編號9的Straight flush）
# Kate 4 （玩家Kate 對應牌型為編號4的Three of a kind）

# 【特別要求】
# 1.如果一副牌中有不合法的輸入，像是不存在的牌面、花色，
# 則輸出 "Error input"(參考 測試資料二)
# 2. 如果一副牌中有重複的牌出現，即一副牌當中有兩張以上牌面跟花色一模一樣，
# 則輸出"Duplicate deal"(參考 測試資料三）
# 3. 如果"Error input"和"Duplicate deal"同時發生，
# 則輸出"Error input"(參考 測試資料四)

# 【測試資料一】
# 輸入:
# 4
# Gery 6D 7C 7S 3H 10S
# Mandy 4H 4D 4C 2D 4S
# Tommy QH KD AC 5D 3S
# Nina 10D 8C 8S 8H 10H
# 輸出:
# Mandy 8
# Nina 7
# Gery 2
# Tommy 1



face_to_value = {
    'A': 1,
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13
}

people_num = int(input())

total_list = {}
all_cards = []
error_flag = False

for _ in range(people_num):
    player_input = input().split()
    player_name = player_input[0]
    cards = player_input[1:]
    new_cards = [[card[:-1], card[-1]] for card in cards]
    for card in new_cards:
        if card[0] not in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            error_flag = True
        elif card[1] not in ['S', 'H', 'D', 'C']:
            error_flag = True
    total_list[player_name] = new_cards
    all_cards.extend(new_cards)

if error_flag:
    print('Error input')
    exit()

all_cards_tuples = [tuple(card) for card in all_cards]
if len(set(all_cards_tuples)) != len(all_cards_tuples):
    print('Duplicate deal')
    exit()

for player in total_list:
    hand = total_list[player]
    for card in hand:
        card[0] = face_to_value[card[0]]
    total_list[player] = sorted(hand, key=lambda x: (x[0], x[1]))
# total_list={'Gery': [[3, 'H'], [6, 'D'], [7, 'C'], [7, 'S'], [10, 'S']], 
#             'Mandy': [[2, 'D'], [4, 'C'], [4, 'D'], [4, 'H'], [4, 'S']], 
#             'Tommy': [[1, 'C'], [3, 'S'], [5, 'D'], [12, 'H'], [13, 'D']], 
#             'Nina': [[8, 'C'], [8, 'H'], [8, 'S'], [10, 'D'], [10, 'H']]}
# print(total_list)

final_list = []

def is_consecutive(ranks):
    card_flag = True
    ranks.sort()
    for ddd in range(1,len(ranks)):
        if ranks[ddd] != ranks[ddd - 1] + 1:
            card_flag =  False
    if ranks == [1, 2, 3, 4, 13] or ranks == [1, 10, 11, 12, 13] or ranks == [1, 2, 11, 12, 13]or ranks == [1,2, 3, 12, 13]:
        card_flag = True
    return card_flag

for i in total_list:
    ranks = [card[0] for card in total_list[i]]
    patterns = [card[1] for card in total_list[i]]
    
    if ranks.count(ranks[0]) == 4 or ranks.count(ranks[4]) == 4:
      # print(i,8)
      final_list.append([i,8])
    elif ranks.count(ranks[0]) == 3 or ranks.count(ranks[4]) == 3 or ranks.count(ranks[2]) == 3:
        if ranks.count(ranks[4]) == 2 or ranks.count(ranks[0]) == 2:
          # print(i,7)
          final_list.append([i,7])
        else:
          # print(i,4)
          final_list.append([i,4])
    elif ranks.count(ranks[0]) == 2 and ranks.count(ranks[3]) == 2 :
        # print(i,3)
        final_list.append([i,3])
    elif ranks.count(ranks[0]) == 2 or ranks.count(ranks[1]) == 2 or ranks.count(ranks[2]) == 2 or ranks.count(ranks[3]) == 2:
        # print(i,2)
        final_list.append([i,2])
    elif is_consecutive(ranks) and patterns.count(patterns[0]) == 5:
        # print(i,9)
        final_list.append([i,9])
    elif is_consecutive(ranks) and patterns.count(patterns[0]) != 5:
        # print(i,5)
        final_list.append([i,5])
    elif not is_consecutive(ranks) and patterns.count(patterns[0]) == 5:
        # print(i,6)
        final_list.append([i,6])
    else:
        # print(i,1)
        final_list.append([i,1])

final_list = sorted(final_list, key = lambda x:(x[1]), reverse = True)
# print(final_list)

for i in final_list:
    print(i[0],i[1])
