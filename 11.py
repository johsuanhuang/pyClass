# A、B、C三本書價格如下，一顧客欲購買A:ｘ本、B:ｙ本、C:ｚ本（ｘ、ｙ、ｚ為使用者輸入），
# 請計算A、B、C各花費多少，以及總共需花費多少錢？

# 定價 1~10本 11~20本 21~30本 31本以上
# A 380 原價 打A1折 打A2折 打A3折
# B 1200 原價 打B1折 打B2折 打B3折
# C 180 原價 打C1折 打C2折 打C3折

# -----------------------------------------------------------------------------------------

# 輸入說明:
# 第一行，A 書本數量(整數,0~100),A1,A2,A3
# 第二行，B 書本數量(整數,0~100),B1,B2,B3
# 第三行，C 書本數量(整數,0~100),C1,C2,C3
# A1~C3為整數0~100，若85為85折，即為*0.85

# 輸出說明:
# 第一行，花費最多的書本名稱、費用(中間以逗號隔開)
# 第二行，花費中間的書本名稱、費用(中間以逗號隔開)
# 第三行，花費最少的書本名稱、費用(中間以逗號隔開)
# 第四行，總費用

# 每本書的費用，最後以無條件進位法到整數。
# 如果兩本書費用相同，按照A>B>C的順序輸出
# 總費用為每本書最後整數費用的加總

# -----------------------------------------------------------------------------------------

# 範例輸入說明
# 6,95,80,75(A書本的數量,A1,A2,A3)
# 12,95,80,70(B書本的數量,B1,B2,B3)
# 30,90,80,75(C書本的數量,C1,C2,C3)

# 範例輸出的說明
# B,13680(花費最多的書本名稱,費用)
# C,4320(花費中間的書本名稱,費用)
# A,2280(花費最少的書本名稱，費用)
# 20280(總金額為13680+4320+2280=20280)


import math




book_obj = {'A': {'price': 380, 
                  'discount': {10: 1.0, 20: 0.9, 30: 0.95, 100: 0.8}, 
                  'books': 1, 
                  'total': 380,
                  'discount_total': 0}, 
            'B': {'price': 1200, 
                  'discount': {10: 1.0, 20: 0.9, 30: 0.8, 100: 0.7}, 
                  'books': 2, 
                  'total': 2400,
                  'discount_total': 0}, 
            'C': {'price': 180, 
                  'discount': {10: 0.98, 20: 0.95, 30: 0.92, 100: 0.9}, 
                  'books': 3, 
                  'total': 540,
                  'discount_total': 0}}

# book_type = book_obj.keys()

discount_rate = [ 20, 30, 100]

for book in book_obj:
    # book_obj[book]['books'] = int(input())
    # book_obj[book]['discount'][20] = float(int(input())) / 100
    # book_obj[book]['discount'][30] = float(int(input())) / 100
    # book_obj[book]['discount'][100] = float(int(input())) / 100
    text = input()
    ittem = text.strip().split(',')
    book_obj[book]['books'] = int(ittem[0])
    book_obj[book]['discount'][20] = float(int(ittem[1])) / 100
    book_obj[book]['discount'][30] = float(int(ittem[2])) / 100
    book_obj[book]['discount'][100] = float(int(ittem[3])) / 100




for book in book_obj:
    book_obj[book]['total'] = book_obj[book]['price'] * book_obj[book]['books']
    # print(book)
    applied_discount = 1
    # for i in book_obj[book]['discount']:
    #     if book_obj[book]['books'] <= i:
    #         book_obj[book]['discount_total'] = math.ceil( book_obj[book]['total'] * book_obj[book]['discount'][i])
    #         break
    quantity = book_obj[book]['books']
    if quantity <= 10:
        applied_discount = 1.0
    elif quantity <= 20:
        applied_discount = book_obj[book]['discount'][20]
    elif quantity <= 30:
        applied_discount = book_obj[book]['discount'][30]
    else:
        applied_discount = book_obj[book]['discount'][100]

    book_obj[book]['discount_total'] = math.ceil(book_obj[book]['total'] * applied_discount)


sorted_data = sorted(book_obj.items(), key=lambda item: item[1]['discount_total'], reverse=True)

dict_data = dict(sorted_data)


total =  sum([dict_data[book]['discount_total'] for book in dict_data])

for book in dict_data:
    print(f"{book},{dict_data[book]['discount_total']}")
print(total)

# print(dict_data) 


# 6,95,80,75
# 12,95,80,70
# 30,90,80,75