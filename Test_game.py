import unittest
from deal import deal
from compare import *
from game_config import *

class GameTestcase(unittest.TestCase):
    "牌的种类"
    def test_judgetype(self):
        #豹子测试
        cardB=["3C","3H","3S"]
        baozi=judgetype(cardB)
        self.assertEquals(baozi,BAOZI)
        #顺子测试
        cardS=["2H","3S","4C"]
        seq=judgetype(cardS)
        self.assertEquals(seq,SEQ)
        #对子测试
        cardP=['2H','2S','4C']
        pair=judgetype(cardP)
        self.assertEquals(pair,PAIR)
        #同花顺测试
        cardcs=['2D','3D','4D']
        CS=judgetype(cardcs)
        self.assertEquals(CS,COLORSEQ)
        #同花测试
        cardC=['4D','5D','8D']
        C=judgetype(cardC)
        self.assertEquals(C,COLOR)
        #单排测试
        cardSi=['3D','8S','7C']
        Si=judgetype(cardSi)
        self.assertEquals(Si,SINGLE)
    "测试单牌比较"
    def test_cmpcard(self):
        x=['3','H']
        y=['2','S']
        tmp=cmpcard(x,y)
        self.assertEquals(tmp,1)
    "发牌并返回获胜者"
    def test_deal(self):
        i=deal(3)
        self.assertIn(i,"012")
unittest.main
