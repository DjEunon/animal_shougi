#!/usr/bin/env python
# -*- coding: utf-8 -*-
from board_str2command import *
import json
import falcon
from datetime import datetime

#クラスを作成し処理を記述する
class TimeResource(object):
    #GETメソッド
    def on_get(self, req, resp):

        #メッセージを記述
        msg = {
            "message": "plz board_str&turn"
        }

        #メッセージをjson形式で返す
        resp.body = json.dumps(msg)
    def on_post(self, req, resp):
        body = req.stream.read()
        #print(body)
        data = json.loads(body)
        
        # パラメーターの取得
        board_str = str(data["board_str"])
        turn=data=str(data["turn"])
        command=board_str2command(board_str,turn)
        msg = {
            "command": command
        }
        resp.body = json.dumps(msg)
#appインスタンス作成
app = falcon.API()
#エンドポイントとクラスを結びつける
app.add_route("/", TimeResource())

if __name__ == "__main__":
    #サーバーを起動する
    from wsgiref import simple_server
    httpd = simple_server.make_server("", 8120, app)
    httpd.serve_forever()