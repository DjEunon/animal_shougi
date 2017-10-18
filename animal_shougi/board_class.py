import re
import itertools

class board_class():
    """description of class"""
    board_origin=""
    board_dictionary={}
    def __init__(self,board_origin):
        if isinstance(board_origin,str):
            self.str2dic(board_origin)
        elif isinstance(board_origin,dictionary):
            self.board_dictionary=board_origin

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


#plan to Loop Unwinding
#ループ展開したほうが絶対早いことに気づいてしまった
 
#def lion_next_position(base_position,player):
#    position_list=[]    
#    alf_list=[]
#    num_list=[]
#    base_position_alf=base_position[0:1]
#    base_position_num=base_position[-1:]
#    if base_position_alf=="A"or base_position_alf=="B" or base_position_alf=="C":
#        if base_position_alf=="A":
#            alf_list.append("A")
#            alf_list.append("B")
#        elif base_position_alf=="B":
#            alf_list.append("A")
#            alf_list.append("B")
#            alf_list.append("C")
#        elif base_position_alf=="C":
#            alf_list.append("B")
#            alf_list.append("C")
#        if (int(base_position_num)-1)>0:
#            num_list.append(int(base_position_num)-1)
#        if (int(base_position_num)+1)<5:
#            num_list.append(int(base_position_num)+1)
#        num_list.append(base_position_num)
#        for i in num_list:
#            for j in alf_list:
#                position_list.append(j+str(i))
#    elif base_position_alf=="D" or base_position=="E":
#        position_list=all_position_list()
#    try:
#        position_list.remove(base_position)    
#    except :
#        pass
    
#    position_list.sort()
#    return position_list

##plan to Loop Unwinding
##ループ展開したほうが絶対早いことに気づいてしまった。おとなしく書き換えることにする
 

#def elephant_next_position(base_position,player):
#    position_list=[]    
#    alf_list=[]
#    num_list=[]
#    base_position_alf=base_position[0:1]
#    base_position_num=base_position[-1:]
#    if base_position_alf=="A"or base_position_alf=="B" or base_position_alf=="C":
#        if base_position_alf=="A":
#            alf_list.append("B")
#        elif base_position_alf=="B":
#            alf_list.append("A")
#            alf_list.append("C")
#        elif base_position_alf=="C":
#            alf_list.append("B")
#        if (int(base_position_num)-1)>0:
#            num_list.append(int(base_position_num)-1)
#        if (int(base_position_num)+1)<5:
#            num_list.append(int(base_position_num)+1)
#        for i in alf_list:
#            for j in num_list:
#                 position_list.append(i+str(j))
#        position_list.sort()
#        return position_list

#def giraffe_next_position(base_position,player):
#    if base_position_alf=="A"or base_position_alf=="B" or base_position_alf=="C":
#        position_list=lion_next_position(base_position,player)
#        for x in elephant_next_position(base_position,player):
#            position_list.remove(x)
#        return position_list
#     elif base_position_alf=="D" or base_position=="E":
#        position_list=all_position_list()
#    return position_list

#all_position_list=[]

#def all_position(args):
#    if len(all_position_list)==0:
#        temp_list=["A","B","C"]
#        for i in temp_list:
#            for j in range(1,5):
#                all_position_list.append(i+str(j))
#    return all_position_lis

##board_class("A1 g2, B1 l2, C1 e2, A2 --, B2 c2, C2 --, A3 --, B3 c1, C3 --, A4 e1, B4 l1, C4 g1,")
#def witch_frame(frame):
#    if frame[-1:]==1:
#        return "Player1"
#    else:
#        return "Player2"