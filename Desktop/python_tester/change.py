# おつりの枚数を計算するプログラム


price = int(input("値段は："))
money = 1000
change =  money - price
print("おつりは{}円".format(change))
while change > 0 :
    if change >= 0 :
        counter_500 = change // 500
        change = change - 500 * counter_500
        # print(change)
    if change >= 100:
        counter_100 = change // 100
        change = change - 100 * counter_100
        # print(change)
    if change >= 50:
        counter_50 = change // 50
        change = change - 50
        # print(change)
    if change >= 10:
        counter_10 = change // 10
        change = change - 10 * counter_10
        # print(change)
    if change >= 5:
        counter_5 = change // 5
        change = change - 5
        # print(change)
    if change > 0:
        counter_1 = change // 1
        change = change - counter_1 * 1
        # print(change)

print("おつりは500円が{}、100円が{}枚、50円が{}枚、10円が{}枚、5円は{}枚、1円は{}枚".format(counter_500, counter_100, counter_50, counter_10, counter_5, counter_1))

