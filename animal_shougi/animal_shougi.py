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

import socket
import re
import socketClient
import checker


se=socketClient.soketClient("localhost")

BUFSIZE = 1024
serverName = "localhost"
#serverName="10.2.72.178"
serverPort = 4444

se.game_connect();
print(se.get_whoami())
print(se.myturn_now())
while True:
    temp=se.send_command(input(""))
    if temp=="game_end":
        break
    else:
        print(temp)