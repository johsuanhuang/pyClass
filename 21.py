# 梭哈類型

# 輸入5張牌，輸出牌型的類別編號，每張牌由牌面與花色組成，牌面與花色的表示如下：

# 牌面： A、2~10、J、Q、K 花色：S (Spade,黑桃),H (Heart,紅心)
# ,D (Diamond,方塊), C (Club,梅花)

# 例如：7S 表示黑桃7

# 牌型編號(編號越大代表牌型越大)：
# (1) High Card : 單一張牌。
# (2) One pair: 兩張牌數字一樣
# (3) Two pairs : 兩組 Pair 的牌。
# (4) Three of a kind : 三張牌數字一樣。
# (5) Straight : 數字連續的五張牌，頭尾相接亦視為Straight。
# 例如[2, 3, 4, 5, 6],..,[Q,K , A, 2, 3], 
# [K , A, 2, 3, 4], [A, 2, 3, 4, 5]。
# (6) Flush : 五張同一花色的牌
# (7) Full House : Three of a Kind 加一個 Pair
# (8) Four of a kind: : 四張牌數字一樣
# (9) Straight flush : 數字連續的五張牌且花色一樣

# 【輸入說明】
# 第一行：輸入一行字串，包含五張牌，每張牌中間以空白隔開
# 範例輸入說明：
# 7S 7H 7D 6C 6S
# （表示 黑桃7 紅心7 方塊7 梅花6 黑桃6）

# 【輸出說明】
# 第一行：輸出一個整數（1~9），表示最大的牌型編號

# 範例輸出說明：
# 7 （對應牌型為編號7的Full house）

# 【特別要求】
# 1. 如果一副牌中有不合法的輸入，像是不存在的牌面、花色，則輸出 "Error input"
# 2. 如果一副牌中有重複的牌出現，即一副牌當中有兩張以上牌面跟花色一模一樣，
# 則輸出"Duplicate deal"
# 3. 如果"Error input"和"Duplicate deal"同時發生，則輸出"Error input"

# 【測試資料一】
# 輸入：
# 5S 5H 5D 5C 5R
# 輸出：
# Error input

face_to_value = {
    'A': 1,
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13
}


cards = input().split()
new_cards = [[i[:-1],i[-1:]] for i in cards]
# new_cards = [['9', 'D'], ['3', 'D'], ['2', 'D'], ['10', 'D'], ['A', 'D']]

# print(new_cards)
for i in new_cards:
    if i[0] not in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
        print('Error input')
        exit()
    elif i[1] not in ['S', 'H', 'D', 'C']:
        print('Error input')
        exit()

for i in new_cards:
    if new_cards.count(i) > 1:
        print('Duplicate deal')
        exit()

for i in new_cards:
    i[0] = face_to_value[i[0]]

# new_cards  = [['5', 'C'], ['5', 'D'], ['5', 'H'], ['5', 'R'], ['5', 'S']]
# 2D 3D 4D 5D 6D 
new_cards = sorted(new_cards, key = lambda x : (x[0], x[1]))
# print(new_cards)

ranks = [card[0] for card in new_cards]
patterns = [card[1] for card in new_cards]

def is_consecutive(ranks):
    card_flag = True
    ranks.sort()
    for ddd in range(1,len(ranks)):
        if ranks[ddd] != ranks[ddd - 1] + 1:
            card_flag =  False
    if ranks == [1, 2, 3, 4, 13] or ranks == [1, 10, 11, 12, 13] or ranks == [1,2, 3, 12, 13]:
        card_flag = True
    return card_flag

# is_consecutive(ranks)
# for ddd in range(1,len(ranks)):
#     # if ranks[ddd] == 13 and ranks[ddd-1] == 1:
#     # if ranks[ddd] != 13:
#     #   if ranks[ddd] +1 != ranks[ddd+1] :
#     #       card_flag = False
#     #       break
#     # elif ranks[ddd] != 13 and ranks[0] != 1 :
#     #     card_flag = False
#     if ranks[ddd] != ranks[ddd - 1] + 1 and not (ranks[ddd] == 1 and ranks[ddd - 1] == 13):
#         card_flag =  False
    

if ranks.count(ranks[0]) == 4 or ranks.count(ranks[4]) == 4:
    print(8)
# elif ranks.count(ranks[0]) == 3 and ranks.count(ranks[4]) == 2:
    
elif ranks.count(ranks[0]) == 3 or ranks.count(ranks[4]) == 3:
    if ranks.count(ranks[4]) == 2 or ranks.count(ranks[0]) == 2:
      print(7)
    else:
      print(4)
elif ranks.count(ranks[0]) == 2 and ranks.count(ranks[3]) == 2 :
    print(3)
elif ranks.count(ranks[0]) == 2 or ranks.count(ranks[1]) == 2 or ranks.count(ranks[2]) == 2 or ranks.count(ranks[3]) == 2:
    print(2)
elif is_consecutive(ranks) and patterns.count(patterns[0]) == 5:
    print(9)
elif is_consecutive(ranks) and patterns.count(patterns[0]) != 5:
    print(5)
elif not is_consecutive(ranks) and patterns.count(patterns[0]) == 5:
    print(6)
else:
    print(1)