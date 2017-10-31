import socket
import re

BUFSIZE = 1024
serverPort = 4444
class soketClient:
        my_whomi=""
        def __init__(self,serverName):
             self.serverName=serverName
            
        def game_connect(self):
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.serverName, serverPort))
            self.s.recv(BUFSIZE).rstrip().decode()

        def send_command(self,command):
            if re.match(r"^q\s*$", command):
                return self.game_end()
            self.s.send((command + "\n").encode())
            msg = self.s.recv(BUFSIZE)
            msg = msg.rstrip()
            return msg.decode()

        def get_whoami(self):
            if self.my_whomi=="":
                self.my_whomi= self.send_command("whoami")[-7:]
            return self.my_whomi

        def myturn_now(self):
            if self.get_whoami()==self.send_command("turn"):
                return True
            else:
                return False

        def game_end(self):
            print("bye")
            self.s.close()
            return "game_end"
        
        def board(self):
            return self.send_command("board")

        def mv(self,first,second):
            return self.send_command("mv "+str(first)+" "+str(second))
        #"A1 --, B1 --, C1 --, A2 l2, B2 e2, C2 --, A3 --, B3 --, C3 --, A4 --, B4 l1, C4 g1,D1 c1,D2 g1,E1 c2,E2 e2","Player1"