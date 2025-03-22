import http
import json
from utils.login import login

flag = False

def fetch_comics(username, password, salt,token,vars,):
    response = api_request(token)
    if response == False:
        token = login(username, password, salt, vars)
        response = api_request(token)
    return flag,response

def api_request(token):
    global flag
    conn = http.client.HTTPSConnection("www.mangacopy.com")
    headers = {
        'Authorization': f'Token {token}'
    }
    conn.request("GET", "/api/v3/member/collect/comics?ordering=-datetime_updated", headers=headers)
    res = conn.getresponse()
    data = res.read()
    if res.status == 401:
        flag = True
        print("token无效!")
        return False
    else :
        return json.loads(data.decode("utf-8"))