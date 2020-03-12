#coding=utf-8
from game_config import *
from collections import Counter

BAOZI = 60     # 三条
COLORSEQ = 50  # 同花顺
COLOR = 40     # 同花
SEQ = 30       # 顺子
PAIR = 20      # 对子
SINGLE = 10    # 单张

# 单张比较
def cmpcard(x, y):
    x_num = MAPPING_LIST_NUM.index(x[0])
    x_col = MAPPING_LIST_COLOR.index(x[1])
    y_num = MAPPING_LIST_NUM.index(y[0])
    y_col = MAPPING_LIST_COLOR.index(y[1])
    if x_num < y_num:
        return -1
    elif x_num > y_num:
        return 1
    else:
        if x_col < y_col:
            return -1
        elif x_col > y_col:
            return 1
        else:
            return 0
def judgetype(cards):
    temp = cards[:]
    if baozi(cards):  # 豹子
        print("豹子")
        return BAOZI
    if color(cards):  # 同色
        if seq(cards):    # 顺子
            print("同花顺")
            return COLORSEQ   # 同花顺
        print ("同花")
        return COLOR    # 同花
    if seq(cards):
        print ("顺子")
        return SEQ
    if pair(cards):
        print("对子")
        return PAIR
    else:
        print ("单张")
        return SINGLE   # 单张
# 三条
def baozi(pokers):
    count = exchange_number(pokers)
    if len(set(count)) == 1:
        return True
# 同花,红的返1，黑的返2
def color(pokers):
    colorlist = exchange_color(pokers)
    ss = set(colorlist)  # set集合判断是否同花
    if len(ss) == 1:
        if list(ss)[0] in [1, 3]:    # 1,3对应C,S  草黑
            return 2
        elif list(ss)[0] in [0, 2]:   # 0,2 对应  方红
            return 1
# 顺子
def seq(pokers):
    count = exchange_number(pokers)
    sortcount = sorted(count)
    if (sortcount[2] == sortcount[1] + 1 and sortcount[1] == sortcount[0] + 1) or (
            sortcount[0] == 2 and sortcount[1] == 3 and sortcount[2] == 14):         # 判断 A 2 3 情况
        return True
# 对子
def pair(pokers):
    count = exchange_number(pokers)
    if count_card(count, 2):
        return True

# 挑出cards中一张数量为n的牌
def count_card(cards, n):
    lis = Counter(cards)    # counter方法：计数
    returns = []
    for r, num in lis.most_common():  # most_common 找出出现频率最高 的方法 返回的是一个dict
        if num == n:
            returns.append(r)
            return returns
    return returns