import json
import requests

payload={
    "name": "shubh"
}

resp=requests.patch("https://reqres.in/api/users/2" ,data=payload)

print(resp)
print(resp.json())

print(resp.headers.get("content-type"))

assert resp.json()['job']== 'api testing'