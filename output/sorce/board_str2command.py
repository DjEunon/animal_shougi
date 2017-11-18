#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import commands
import re
import itertools
import sys
import board_class

class board_class():
    """description of class"""
    board_origin=""
    board_dictionary={}
    board_turn=""
    
    def __init__(self,board_origin,turn):
        if isinstance(board_origin,str):
            self.str2dic(board_origin)
        elif isinstance(board_origin,dictionary):
            self.board_dictionary=board_origin
        self.board_turn=turn
    def all_clear(self):
        self.board_origin=""
        self.board_turn=""
        self.board_dictionary.clear()
    def str2dic(self,string_board):
        self.board_origin=string_board
        temp_list=[]
        temp_list=self.board_origin.split(",")
        for x in temp_list:
            x=re.sub(r'^\ ',"",x)
            key=x[0:2]
            val=x[-2:]
            if key!='' and val!='':
                self.board_dictionary[key]=val
    def get_board_origin(self):
        return self.board_origin

    def get_board_dictionary(self):
        return self.board_dictionary

    def get_next_board(self,turn):
        pass

    def exchange_format(self):
        return_str=""
        p1h=0
        p1z=0
        p1k=0
        p2h=0
        p2z=0
        p2k=0
        for x in '1234':
            for y in 'ABC':
                temp=self.board_dictionary[str(y)+str(x)]
                if temp=="--":
                    return_str+=" . "
                else:
                    alf_temp=temp[0:1]
                    num_temp=temp[-1:]
                    if num_temp=="1":
                        return_str+="+"
                    else:
                        return_str+="-"
                    
                    if alf_temp=="l":
                        return_str+="LI"
                    elif alf_temp=="g":
                        return_str+="KI"
                    elif alf_temp=="e":
                        return_str+="ZO"
                    elif alf_temp=="c":
                        return_str+="HI"
                    elif alf_temp=="h":
                        return_str+="NI"
            return_str+="\n"
        for x in '123456':
            for y in 'DE':
                if str(y)+str(x) in self.board_dictionary:
                    temp=self.board_dictionary[str(y)+str(x)]
                    alf_temp=temp[0:1]
                    num_temp=temp[-1:]
                    if y=="D":
                        if alf_temp=="g":
                            p1k+=1
                        elif alf_temp=="e":
                            p1z+=1
                        elif alf_temp=="c":
                            p1h+=1
                    else:
                        if alf_temp=="g":
                            p2k+=1
                        elif alf_temp=="e":
                            p2z+=1
                        elif alf_temp=="c":
                            p2h+=1
        return_str+=str(p1h)+str(p1z)+str(p1k)+str(p2h)+str(p2z)+str(p2k)
        return_str+="\n"
        if self.board_turn=="Player1":
            return_str+="+"
        else :
            return_str+="-"
        return return_str
    def get_turn(self):
        return self.board_turn




def exchange_koma(koma):
    if koma=="ZO":
        return "e"
    elif koma=="KI":
        return "g"
    elif koma=="LI":
        return "l"
    elif  koma=="HI":
        return "c"
    elif koma=="NI":
        return "h"

def board_str2command(board_str,turn):
    
    #bo=board_class(board_str,turn)
    #bo=board_class("A1 --, B1 --, C1 --, A2 l2, B2 e2, C2 --, A3 --, B3 --, C3 --, A4 --, B4 l1, C4 g1,D1 c1,D2 g1,E1 c2,E2 e2","Player1")
    bo=board_class(board_str,turn)
    bo.all_clear()
    bo=board_class(board_str,turn)
    f=open("kyokumen.txt",'w')
    strin=bo.exchange_format()
    
    #print(strin)
    f.write(strin)
    f.close()
    cmdstd=commands.getoutput("./checkState ./kyokumen.txt")
    #cmdstd=commands.getoutput("./checkState "+strin)
    lis=cmdstd.rsplit("\n")

    f_move=""

    for x in lis:
        if x[0:4]=="Move":
            f_move=x[8:14]
            break
	
    #print(f_move)	
    if str(f_move[0:2])=="00":
        alf=""
        dic=bo.get_board_dictionary()
        if bo.get_turn()=="Player1":
            for x in '123456':
                if "D"+str(x) in dic:
                    if dic["D"+str(x)][0:1]==exchange_koma(f_move[-2:]):
                        alf="D"+str(x)
        else:
            for x in '123456':
                if "E"+str(x) in dic:
                    if dic["E"+str(x)][0:1]==exchange_koma(f_move[-2:]):
                        alf="E"+str(x)
        cmd=("mv "+alf+" "+f_move[2:4])
    else:
        cmd=("mv "+f_move[0:2]+" "+f_move[2:4])
	#print(cmd)
    return cmd
#bo=board_class("A1 g2, B1 --, C1 l2, A2 c2, B2 c1, C2 --, A3 --, B3 --, C3 e1, A4 e1, B4 l1, C4 g1,","Player1")
#print(bo.exchange_format())
