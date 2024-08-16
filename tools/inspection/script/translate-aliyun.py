import requests
import json
import sys

api_key = sys.argv[1]
base_url = sys.argv[2]
#base_url = "http://127.0.0.1:80"
url = base_url + "/v1/translate" #通过base_url拼接请求的url

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