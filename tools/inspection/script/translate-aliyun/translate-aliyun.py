import requests
import json
import sys

api_key = sys.argv[1]
base_url = sys.argv[2]
#base_url = "http://43.144.248.160:80"
#网关内的 url 为： http://ip:80/v1/translate
#网关外的 url 为：  http://ip:80/api/v1/translate
url = base_url #通过base_url拼接请求的url

json_data = {"parameter":{
    'text': ['我预定了一个房间，这是我的订单信息'],
    'from': 'zh',
    'to': 'en'
}
}
response = requests.post(url, json=json_data)
if response.status_code != 200:
    print(f"fail\tstatus code is {response.status_code}")
else:
    try:
        response_json = response.json()
        if len(response_json) == 0:
            print(f"fail\tno translate")
        elif response_json["trans_results"][0] != 'I have reserved a room. This is my order information.':
            print(f"fail\ttranslate result is: {response_json[0]}")
        else:
            print("success\tok")
    except Exception as e:
        print("fail\tdecode json error")