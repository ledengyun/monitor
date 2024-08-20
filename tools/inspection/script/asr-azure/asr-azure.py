import requests
import json
import sys
import websocket
import os
api_key = sys.argv[1]
base_url = sys.argv[2]

url = base_url + "/recognition" #通过base_url拼接请求的url
base_file_path=os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_file_path,"test.wav")
ws = websocket.create_connection(url)

with open(file_path, 'rb') as file:
    binary_data = file.read()
data_biany = binary_data
ws.send_binary(data_biany)

re_data = ws.recv()

if ws.status != 101 :
    print(f"fail\t asr-azure status code is {ws.status}")
else:
    try:
        res_json = json.loads(re_data)
        if "asr_results" not in res_json:
            print(f"fail\tasr-azure")
        elif res_json["asr_results"]["text"] !='确保一切顺利，确保一切顺利。':
            print(f"fail\tasr-azure result is: {res_json}")
        else:
            print("success\tok")
    except Exception as e:
        print("fail\tdecode json error")
        print(e)