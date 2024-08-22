import requests
import json
import sys
import os
api_key = sys.argv[1]
base_url = sys.argv[2]

#base_url = "http://127.0.0.1:80"
#

#base_file_path="/Users/4paradigm/Downloads"
#网关内url  http://ip:port/document-analysis
#网关外url  http://ip:port/api/v1/document-analysis
url = base_url  #通过base_url拼接请求的url
base_file_path=os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_file_path,"zh_en.png")
payload={}
files=[
   ('file',('zh_en.png',open(file_path,'rb'),'image/png'))
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
