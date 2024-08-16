import requests
import json
import sys

api_key = sys.argv[1]
base_url = sys.argv[2]
base_file_path="tools/inspection/script/ocr-azure"
#base_url = "http://127.0.0.1:80"
#

#base_file_path="/Users/4paradigm/Downloads"
url = base_url + "/api/v1/document-analysis" #通过base_url拼接请求的url

payload={}
files=[
   ('file',('zh_en.png',open(f'{base_file_path}/zh_en.png','rb'),'image/png'))
]

response = requests.request("POST", url,  data=payload, files=files)
if response.status_code != 200:
    print(f"fail\tstatus code is {response.status_code}")
else:
    try:
        response_json = response.json()
        if len(response_json) == 0:
            print(f"fail\tno ocr-azure")
        else:
            print("success\tok")
    except Exception as e:
        print("fail\tdecode json error")
