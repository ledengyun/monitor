import requests
import json
import sys

api_key = sys.argv[1]
base_url = sys.argv[2]
#base_url = "http://127.0.0.1:80"
url = f'{base_url}/api/v1/generation/summarization' #通过base_url拼接请求的url

json_data = {
    "content": "这是一个产品研讨的会议,本次会议我们主要讨论了产品该如何推向市场，产品该如何进行设计以及产品该如何研发。"
}
response = requests.post(url, json=json_data)
if response.status_code != 200:
    print(f"fail\tstatus code is {response.status_code}")
else:
    try:
        response_json = response.json()
        if len(response_json) == 0:
            print(f"fail\ttext-summarization")
        elif ("summarization" not in response_json) and ("paragraphSummary" not in response_json["summarization"]) :
            print(f"fail\ttext-summarization is: {response_json}")
        else:
            print("success\tok")
    except Exception as e:
        print("fail\tdecode json error")
