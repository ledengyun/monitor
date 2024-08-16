import requests
import json
import sys
import websocket
#api_key = sys.argv[1]
#base_url = sys.argv[2]
#base_file_path = sys.argv[3]
base_url = "ws://127.0.0.1:80"
url = base_url + "/stream/tts" #通过base_url拼接请求的url

ws = websocket.create_connection(url)

start_param={
      "language":"zh",
      "voice_name": "zh-m-standard-1",
      "sample_rate": 16000
}
ws.send_text(json.dumps(start_param,ensure_ascii=False))
start_re_data = ws.recv()
print(start_re_data)
start_re_data_json = json.loads(start_re_data)
if not start_re_data_json["success"]:
    print(f"fail\t text2speech-azure init")

data_json = {
    "text": "今天天气真好"
}
ws.send_text(json.dumps(data_json,ensure_ascii=False))
re_data = ws.recv()
if ws.status != 101 :
    print(f"fail\t text2speech-azure status code is {ws.status}")
else:
    try:
        res_json = json.loads(re_data)
        if ("data" not in res_json) or ("audio_block_seq" not in res_json) or ("audio_status" not in res_json):
            print(f"fail\ttext2speech-azure")
        elif res_json["audio_status"] !=1:
            print(f"fail\ttext2speech-azure result is: {res_json}")
        else:
            print("success\tok")
    except Exception as e:
        print("fail\tdecode json error")
        print(e)