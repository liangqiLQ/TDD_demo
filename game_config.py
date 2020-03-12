
import random
# 花色 红黑方梅
SUITS = ['H', 'S', 'D', 'C']
#方片 D 黑桃 S 红桃 H 梅花 C
# 初始基本牌
INIT_LIST = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q','K','A']

MAPPING_LIST_NUM = '23456789TJQKA'
MAPPING_LIST_COLOR = 'DCHS'  # 方梅红黑
#初始牌堆
def init_landlords():
    lis = []
    for card in INIT_LIST:  # 数字
        for suit in SUITS:  # 花色
            lis.append('{0}{1}'.format(card, suit))
    random.shuffle(lis)
    # print(lis)
    return lis

    # print "初始化牌堆：", lis

def exchange_number(cards):
    number = []
    for r, s in cards:
        temp = MAPPING_LIST_NUM.index(r)
        number.append(temp)
    return number


def exchange_color(cards):
    color = []
    for r, s in cards:
        temp = MAPPING_LIST_COLOR.index(s)
        color.append(temp)
    return color



if __name__ =='__main__':
    init_landlords()

