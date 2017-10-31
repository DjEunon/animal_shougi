# -*- coding: utf-8 -*-

#　　 ＿＿
#　 ／―＜／)
#　/ ＿　 二フ　　＿
#`ヘ(●)　　ﾉ　 ／ /
#(＿)￣_フ＜＿_/ ∠＿
#　　＞／￣￣フ∠＿／
#　 幺(　　　フ＿＿＞
#　 ヽ ＼＿＿＞ノ
#　　 ＼＿＿＿ノ
#　　　 ＿))ﾆ)
#　　 ∠∠)＿＞
#   chocobo-is-food 

import random
import socket
import re
import socketClient
import checker
import board_class
import post_client
from post_client import *
import time


def get_f(flame):
    return flame[:1]

def witch_frame(frame):
    if frame[-1:]=="1":
        return "Player1"
    else:
        return "Player2"

def lion_next_position(base_position,player):
    position_list=[]    
    alf_list=[]
    num_list=[]
    base_position_alf=base_position[0:1]
    base_position_num=base_position[-1:]
    if base_position_alf=="A"or base_position_alf=="B" or base_position_alf=="C":
        if base_position_alf=="A":
            alf_list.append("A")
            alf_list.append("B")
        elif base_position_alf=="B":
            alf_list.append("A")
            alf_list.append("B")
            alf_list.append("C")
        elif base_position_alf=="C":
            alf_list.append("B")
            alf_list.append("C")
        if (int(base_position_num)-1)>0:
            num_list.append(int(base_position_num)-1)
        if (int(base_position_num)+1)<5:
            num_list.append(int(base_position_num)+1)
        num_list.append(base_position_num)
        for i in num_list:
            for j in alf_list:
                position_list.append(j+str(i))
    elif base_position_alf=="D" or base_position=="E":
        position_list=all_position_list()
    try:
        position_list.remove(base_position)    
    except :
        pass
    
    position_list.sort()
    return position_list

#plan to Loop Unwinding
#ループ展開したほうが絶対早いことに気づいてしまった。おとなしく書き換えることにする
 

def elephant_next_position(base_position,player):
    position_list=[]    
    alf_list=[]
    num_list=[]
    base_position_alf=base_position[0:1]
    base_position_num=base_position[-1:]
    if base_position_alf=="A"or base_position_alf=="B" or base_position_alf=="C":
        if base_position_alf=="A":
            alf_list.append("B")
        elif base_position_alf=="B":
            alf_list.append("A")
            alf_list.append("C")
        elif base_position_alf=="C":
            alf_list.append("B")
        if (int(base_position_num)-1)>0:
            num_list.append(int(base_position_num)-1)
        if (int(base_position_num)+1)<5:
            num_list.append(int(base_position_num)+1)
        for i in alf_list:
            for j in num_list:
                 position_list.append(i+str(j))
        position_list.sort()
        return position_list

def giraffe_next_position(base_position,player):
    base_position_alf=base_position[0:1]
    base_position_num=base_position[-1:]
    if base_position_alf=="A"or base_position_alf=="B" or base_position_alf=="C":
        position_list=lion_next_position(base_position,player)
        for x in elephant_next_position(base_position,player):
            position_list.remove(x)
        return position_list
    

all_position_list=[]

def all_position(args):
    if len(all_position_list)==0:
        temp_list=["A","B","C"]
        for i in temp_list:
            for j in range(1,5):
                all_position_list.append(i+str(j))
    return all_position_lis

se=socketClient.soketClient("localhost")

board_all_list=[]
se.game_connect();
while True:
    if se.myturn_now():
        #print(se.send_command("board"))
        se.send_command(post_send_localserver(se.send_command("board"),se.get_whoami()))
    #if True:


    #    if se.myturn_now:
    #       bo=board_class.board_class(se.send_command("board"))
          
    #       board_all_list.append(bo.get_board_dictionary())
    #       cha=str(random.choice('ABC'))+str(random.choice('1234'))
    #       cho=board_all_list[-1][cha]
          
    #       check_lion=board_all_list[-1].values
    #       aaa=False
    #       for x in ["A","B","C"]:
    #           for y in ["1","2","3","4"]:
    #               if board_all_list[-1][x+y]=="l"+se.get_whoami()[-1]:
    #                    aaa=True   

    #       if aaa==False:               
    #           print("反則検知（多分・・・）")
    #           input()
    #       #print(witch_frame(cho))
    #       #print(se.get_whoami())
    #       if witch_frame(cho)==se.get_whoami():
                
    #            if get_f(cho)=="l":
    #                    a=[]
    #                    a=lion_next_position(cha,se.get_whoami())
    #                    random.shuffle(a)
    #                    se.send_command("mv "+cha+" "+a[0])  
    #            elif get_f(cho)=="g":
    #                    a=[]
    #                    a=giraffe_next_position(cha,se.get_whoami())
    #                    random.shuffle(a)
    #                    se.send_command("mv "+cha+" "+a[0])
    #            elif get_f(cho)=="e":
    #                    a=[]
    #                    a=elephant_next_position(cha,se.get_whoami())
    #                    random.shuffle(a)
    #                    se.send_command("mv "+cha+" "+a[0])
    #    else:
    #        pass



