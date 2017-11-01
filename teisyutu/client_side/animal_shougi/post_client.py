import urllib.request, json


def post_send_localserver(string,turn):
    url = "http://192.168.198.135:8120/" 
    method = "POST"
    headers = {"board_str" : "json"}
    # PythonオブジェクトをJSONに変換する
    obj = {'board_str' : string, 'turn' : turn}
    
    json_data = json.dumps(obj).encode("utf-8")
    # httpリクエストを準備してPOST
    request = urllib.request.Request(url, data=json_data, method=method, headers=headers)
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
        return json.loads(response_body)["command"]