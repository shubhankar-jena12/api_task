import json
import requests
"""
mydata=open("data.json" , "r").read()
resp=requests.post("https://reqres.in/api/users" , data=json.loads(mydata))
"""

resp=requests.post("https://reqres.in/api/users", data=json.loads(open("data.json", "r").read()))

print(resp)
print(resp.json())

print(resp.headers.get("content-type"))

assert resp.json()['name']== 'shubhankar'