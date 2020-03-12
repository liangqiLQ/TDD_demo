#coding=utf-8
from game_config import *
from functools import cmp_to_key
from compare import *
from compare import *
from operator import itemgetter
#发牌
def deal(player_num):
    lis = init_landlords()
    seat = 0
    tile_list = []
    if player_num <= 6 and player_num >=2:
        while seat < player_num:
            tile = []
            rounds = 0
            while rounds < 3:
                tile.append(lis.pop())  # tile中三张
                rounds += 1
            tile_list.append(tile)  # tile_list中  3张*人数
            seat += 1
    elif player_num < 0:
        print ("玩家人数错误")
        return
    elif player_num >= 0 and player_num <= 1:
        print ("人数不够")
        return
    else:
        print ("人数超过")
        return
    # 牌排序后分发到玩家手中
    card_group = []
    group_type = []
    seat_list = []
    for key, value in enumerate(tile_list):
        # print player,value
        card_group.append(sorted(value, key=cmp_to_key(cmpcard)))
        seat_list.append(key)
    # print "发%d个人的牌:"%player_num,card_group
    for key, value in enumerate(card_group):
        s = judgetype(value)
        print(s)
        group_type.append(s)  # 玩家三张牌的牌型
        print("玩家%d的牌 ：" % key ,value,s)
        print ("______________________________________")
        # dic_score[key] = s
    # print card_group,group_type
    # print "玩家的牌型:",group_type
    player_card = list(zip(seat_list,card_group,group_type))

    cmp_data = []
    for i in range(len(player_card)):
        data_i = player_card[i]
        player_seat = data_i[0]
        card_list = data_i[1]
        card_type = data_i[2]
        max_card = max(card_list, key=lambda x: MAPPING_LIST_NUM.index(x[0]))
        cmp_data.append([card_type, MAPPING_LIST_NUM.index(max_card[0]), MAPPING_LIST_COLOR.index(max_card[1]), data_i])
        # print cmp_data
    result = sorted(cmp_data, key=itemgetter(0, 1, 2))
    sorted_list = []
    # print result
    for res in result:
        sorted_list.append(res[3])
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("本局牌最大的是 :     玩家{0}".format(sorted_list[-1][0]))
    return str(sorted_list[-1][0])
if __name__ == '__main__':
    deal(3)
