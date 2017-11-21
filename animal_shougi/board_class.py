import re
from copy import deepcopy
import itertools
import copy

class board_class():
    """description of class"""
    board_origin=""
    board_dictionary={}
    all_position_list=[]
    move_possible_list_normal=[]
    move_possible_list_special=[]
    board_turn=""
    
    def __init__(self,board_origin,turn):
        if isinstance(board_origin,str):
            self.str2dic(board_origin)
        elif isinstance(board_origin,dict):
            self.board_dictionary=board_origin
        self.board_turn=turn

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


        return None
    
    def get_board_turn(self):
        return self.board_turn

    def get_board_origin(self):
        return self.board_origin

    def get_board_dictionary(self):
        return self.board_dictionary

    def get_next_board(self):
        next_turn=""
        if self.board_turn=="Player1":
            next_turn=="Player2"
        else:
            next_turn=="Player1"
        piece_temp=""
        pice_er_temp=""
        animal_temp=""
        next_list=[]
        compare_list=[]
        dic_temp={}
        list_temp=[]
        for x in 'ABCDE':
            for y in '123456':

                list_temp.clear()
                dic_temp.clear()
                compare_list.clear()
                if str(x)+str(y) in self.board_dictionary:
                    if self.get_board_turn()==self.__piece_turn_decision(self.board_dictionary[str(x)+str(y)]):
                        piece_temp=self.board_dictionary[str(x)+str(y)]
                        animal_temp=self.__animal_decision(piece_temp)
                        if animal_temp=="lion":
                            list_temp.extend(self.__lion_next_position(str(x)+str(y)))
                        elif animal_temp=="giraffe":
                            list_temp.extend(self.__giraffe_next_position(str(x)+str(y)))
                        elif animal_temp=="chick":
                            list_temp.extend(self.__chick_next_position(str(x)+str(y)))
                        elif animal_temp=="chicken":
                            list_temp.extend(self.__chicken_next_position(str(x)+str(y)))
                        elif animal_temp=="elephant":
                            list_temp.extend(self.__elephant_next_position(str(x)+str(y))) 
                        elif animal_temp==False:
                            pass
                if str(x)+str(y) in self.board_dictionary:
                    #print(self.board_dictionary[str(x)+str(y)])
                    pass
                if len(list_temp)>0:
                    dic_temp=copy.deepcopy(self.board_dictionary)
                    dic_temp[str(x)+str(y)]="--"
                    compare_list.extend(self.__list_compare(self.__move_possible_special(),list_temp))
                    if len(compare_list)>0:
                        for z in compare_list:
                            dic_temp.clear()
                            dic_temp=copy.deepcopy(self.board_dictionary)
                            dic_temp[str(x)+str(y)]="--"
                            dic_temp[z]=piece_temp
                            list_temp.remove(z)
                            next_list.append(board_class(dic_temp,next_turn))
                            print(dic_temp)
                    print(list_temp)
                    for z in list_temp:
                        pice_er_temp=self.board_dictionary[z]
                        dic_temp.clear()
                        dic_temp=copy.deepcopy(self.board_dictionary)
                        dic_temp[str(x)+str(y)]="--"
                        dic_temp[z]=piece_temp
                        al_temp=""
                        if self.__piece_turn_decision(pice_er_temp)=="Player1":
                            al_temp="E"
                        else:
                            al_temp="D"
                        #sorting
                        for a in '123456':
                            if str(al_temp)+str(a) not in dic_temp:
                                dic_temp[str(al_temp)+str(a)]=pice_er_temp[0:1]+self.piece_uragiri(pice_er_temp)[-1:]
                                break
                            if str(al_temp)+str(a) in dic_temp:
                                if dic_temp[str(al_temp)+str(a)]=="--":
                                     dic_temp[str(al_temp)+str(a)]=pice_er_temp[0:1]+self.piece_uragiri(pice_er_temp)[-1:]
                                     break
                        print(dic_temp)
                                



    def piece_uragiri(self,p):
        if self.__piece_turn_decision(p)=="Player1":
            return "Player2"
        else:
            return "Player1"

    def de_nanon(self,d):
        be=d[0:1]
        if be=="D" or be=="E":
            return True
        else:
            return False

    def d_nanon(self,d):
        be=d[0:1]
        if be=="D":
            return True
        else:
            return False
        pass

    

    def exchange_format(self):
        pass
    def __chicken_next_position(self,base_position):
        position_list=[]
        position_list.extend(self.__chick_next_position(base_position))
        position_list.extend(self.__elephant_next_position(base_position))

        return position_list

    def __chick_next_position(self,base_position):
        position_list=[]
        alf_list=[]
        num_list=[]
        base_position_alf=base_position[0:1]
        base_position_num=int(base_position[-1:])
        vector=""
        if self.board_turn=="Player1":
            vector=-1
        elif self.board_turn=="Player2":
            vector=1
        else:
            pass

        if base_position_alf=="A":
            if int(base_position_num+vector) > 0 and int(base_position_num+vector) < 5:
                position_list.append("A"+str(int(base_position_num+vector)))

        elif base_position_alf=="B":
            if int(base_position_num+vector)>=1 and int(base_position_num+vector)<=4:
                position_list.append("B"+str(int(base_position_num+vector)))

        elif base_position_alf=="C":
            if int(base_position_num+vector)>=1 and int(base_position_num+vector)<=4:
                position_list.append("C"+str(int(base_position_num+vector)))
        
        elif base_position_alf=="D" or base_position_alf=="E":
            position_list=self.__move_possible_special()
            ##奥に飛んでいかない処理
            if self.get_board_turn()=="Player1":
                if "C1" in position_list:
                    position_list.remove("C1")
                if "A1" in position_list:
                    position_list.remove("A1")
                if "B1" in position_list:
                    position_list.remove("B1")
            elif self.get_board_turn()=="Player2":
                if "C4" in position_list:
                    position_list.remove("C4")
                if "A4" in position_list:
                    position_list.remove("A4")
                if "B4" in position_list:
                    position_list.remove("B4")
            try:
                position_list.remove(base_position)    
            except :
                pass
        
        return position_list
    def __dictionary_exchanger(self,dic):
        d_list=[]
        e_list=[]
        for x in 'DE':
            for y in '123456':
                if x+y not in dic:
                    dic[x+y]="--"
        for x in '123456':
            if dic["D"+x]!="--":
                d_list.append(dic["D"+x])
                dic["D"+x]="--"
        for x in '123456':
            if dic["E"+x]!="--":
                e_list.append(dic["E"+x])
                dic["E"+x]="--"

        


    def __lion_next_position(self,base_position):
        position_list=[]
        position_temp_list=[]
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
                    position_temp_list.append(j+str(i))
            position_list.extend(self.__list_compare(self.__move_possible_normal(),position_temp_list))
        elif base_position_alf=="D" or base_position_alf=="E":
            position_list=move_possible_list_special()
        try:
            position_list.remove(base_position)    
        except :
            pass
    
        position_list.sort()
        return position_list

    def __elephant_next_position(self,base_position):
        position_list=[]
        position_temp_list=[]
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
                     position_temp_list.append(i+str(j))
            position_list.append(self.__list_compare(self.__move_possible_normal(),position_temp_list))
        elif base_position_alf=="D" or base_position_alf=="E":
            position_temp_list=self.__move_possible_special()
            position_list.append(self.__list_compare(self.__move_possible_special(),position_temp_list))
        try:
            position_list.remove(base_position)    
        except :
            pass
        position_list.sort()
        return position_list[0]
    
    def __giraffe_next_position(self,base_position):
        position_list=[]
        position_temp_list=[]
        alf_list=[]
        num_list=[]
        base_position_alf=base_position[0:1]
        base_position_num=base_position[-1:]

        if base_position_alf=="A"or base_position_alf=="B" or base_position_alf=="C":
            position_list=self.__lion_next_position(base_position)
            for x in self.__elephant_next_position(base_position):
                try:
                    position_list.remove(x)
                except:
                    pass
            return position_list
        elif base_position_alf=="D" or base_position_alf=="E":
            position_list=__move_possible_special()

        return position_list

    def __all_position(self):
        if len(self.all_position_list)==0:
            temp_list=["A","B","C"]
            for i in temp_list:
                for j in range(1,5):
                    self.all_position_list.append(i+str(j))
        return self.all_position_list
    def __all_position_possible(self):
        position_list=[]
        position_list.extend(self.__all_position())
        
        


    def __animal_decision(self,piecestr):
        fstr=self.__get_firststr(piecestr)
        if fstr=="e":
            return "elephant"
        elif fstr=="g":
            return "giraffe"
        elif fstr=="l":
            return "lion"
        elif fstr=="c":
            return "chick"
        elif fstr=="h":
            return "chicken"
        return False

#    def __animal_move_possible(self,position_list,now_position,piece_animal):
#        pass

    def __move_possible_normal(self):
        for x in 'ABC':
            for y in '1234':
                if str(x)+str(y) not in self.board_dictionary:
                    self.move_possible_normal_list.append(str(x)+str(y))
        for x in 'ABC':
            for y in '1234':
                if str(x)+str(y) in self.board_dictionary:
                    if self.__piece_turn_decision(self.board_dictionary[str(x)+str(y)])!=self.get_board_turn():
                        self.move_possible_list_normal.append(str(x)+str(y))
        self.move_possible_list_normal.extend(self.__move_possible_special())
        return list(set(self.move_possible_list_normal))
    
    def __move_possible_special(self):
        for x in 'ABC':
            for y in '1234':
                if str(x)+str(y) not in self.board_dictionary:
                    self.move_possible_normal_list.append(str(x)+str(y))
        for x in 'ABC':
            for y in '1234':
                if str(x)+str(y) in self.board_dictionary:
                    if self.board_dictionary[str(x)+str(y)]=="--":
                        self.move_possible_list_special.append(str(x)+str(y))
        return list(set(self.move_possible_list_special))

    def __piece_turn_decision(self,piece):
        if piece[-1:]=="1":
            return "Player1"
        else:
            return "Player2"

    def __get_firststr(self,fstr):
        return fstr[0:1]
    
    def __list_compare(self,list1,list2):
        list1_set=set(list1)
        list2_set=set(list2)
        return list(list1_set&list2_set)

    def test_print(self):
        self.get_next_board()
    def killing_you(self):
        tple_temp=self.board_dictionary.items()
        r_temp=""
        retunlist=[]
        if self.get_board_turn()[-1:]=="1":
            for x in tple_temp:
                if x[1]=="l2":
                    lion_temp=x[0]
            for x in tple_temp:
                if x[1][-1:]=="1":
                    anm_temp=self.__animal_decision(x[1][0:1])
                    if self.de_nanon(x[0]):
                        pass
                    elif anm_temp=="elephant":
                        for y in self.__elephant_next_position(x[0]):
                            if lion_temp==y:
                                r_temp=x[0]
                    elif anm_temp=="giraffe":
                        for y in self.__giraffe_next_position(x[0]):
                            if lion_temp==y:
                                r_temp=x[0]
                    elif anm_temp=="lion":
                        for y in self.__lion_next_position(x[0]):
                            if lion_temp==y:
                                r_temp=x[0]
                    elif anm_temp=="chick":
                        for y in self.__chick_next_position(x[0]):
                            if lion_temp==y:
                                r_temp=x[0]
                    elif anm_temp=="chicken":
                        for y in self.__lion_next_position(x[0]):
                            if lion_temp==y:
                                r_temp=x[0]
            
            retunlist=[str(lion_temp),str(r_temp)]
            return retunlist
        elif self.get_board_turn()[-1:]=="2":
            for x in tple_temp:
                if x[1]=="l1":
                    lion_temp=x[0]
            for x in tple_temp:
                if x[1][-1:]=="2":
                    anm_temp=self.__animal_decision(x[1][0:1])
                    if self.de_nanon(x[0]):
                        pass
                    elif anm_temp=="elephant":
                        for y in self.__elephant_next_position(x[0]):
                            if lion_temp==y:
                                r_temp=x[0]
                    elif anm_temp=="giraffe":
                        for y in self.__giraffe_next_position(x[0]):
                            if lion_temp==y:
                                r_temp=x[0]
                    elif anm_temp=="lion":
                        for y in self.__lion_next_position(x[0]):
                            if lion_temp==y:
                                r_temp=x[0]
                    elif anm_temp=="chick":
                        for y in self.__chick_next_position(x[0]):
                            if lion_temp==y:
                                r_temp=x[0]
                    elif anm_temp=="chicken":
                        for y in self.__lion_next_position(x[0]):
                            if lion_temp==y:
                                r_temp=x[0]
            
            retunlist=[str(lion_temp),str(r_temp)]
            return retunlist
            


bo=board_class("A1 g2, B1 l2, C1 e2, A2 --, B2 c2, C2 --, A3 --, B3 c1, C3 --, A4 e1, B4 l1, C4 g1, D1 --,D2 --","Player2")
bo.test_print()
