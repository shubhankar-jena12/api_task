import json
import requests

payload={
    "name": "shubhankar",
    "job automation": "automation"
}
print(type(payload))

resp=requests.post("https://reqres.in/api/users" , data=payload)
print(resp)
print(resp.json())
assert resp.json()["name"]=="shubhankar"