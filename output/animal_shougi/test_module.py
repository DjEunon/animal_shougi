import socket
import re
import socketClient
import checker


se=socketClient.soketClient("localhost")

se.game_connect();
print(se.get_whoami())
print(se.myturn_now())
while True:
    temp=se.send_command(input(""))
    if temp=="game_end":
        break
    else:
        if se.myturn_now:
            pass