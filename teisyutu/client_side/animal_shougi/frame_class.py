import random
import socket
import re
import socketClient
import checker
import post_client
import board_class
from post_client import *
import time

class piece_class():
    position=""
    piece=""
    player=""

    def __init__(self,position,piece_all):
        self.position=position
        self.piece=piece_all[0:1]
        if str(piece_all[-1:])=="1":
            self.player="Player1"
        elif str(piece_all[-1:])=="2":
            self.player="Player2"



fr=piece_class("A2","g2")